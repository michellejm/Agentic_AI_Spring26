"""
What Did I Work On? — A work history agent built with LangChain.

Scans a folder of emails, calendar entries, and markdown notes, then
answers questions about your work history using Claude with tool use.

Usage:
    python agent.py [--data-dir PATH]

Data directory layout (all optional):
    data/
        emails/      ← .eml, .txt, .md files
        calendar/    ← .ics, .txt, .md files
        notes/       ← .md, .txt files

Set ANTHROPIC_API_KEY in your environment before running.
"""

import os
import re
import glob
import argparse

from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent

# ---------------------------------------------------------------------------
# Data directory (set before tools are defined)
# ---------------------------------------------------------------------------

DATA_DIR = "data"  # overridden by --data-dir at startup


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------

@tool
def list_files(category: str = "") -> str:
    """List all work files in the data directory.
    Use category to narrow to 'emails', 'calendar', or 'notes'.
    Leave category empty to list everything.
    """
    search_path = os.path.join(DATA_DIR, category, "**", "*") if category \
        else os.path.join(DATA_DIR, "**", "*")

    files = [f for f in glob.glob(search_path, recursive=True) if os.path.isfile(f)]
    if not files:
        return f"No files found in {search_path!r}."

    rel = [os.path.relpath(f, DATA_DIR) for f in sorted(files)]
    return "\n".join(rel)


@tool
def read_file(path: str) -> str:
    """Read the full contents of a file. Path is relative to the data directory,
    e.g. 'emails/2024-03-sprint-kickoff.txt'.
    """
    abs_path = path if os.path.isabs(path) else os.path.join(DATA_DIR, path)

    # Safety: keep reads inside DATA_DIR
    real_data = os.path.realpath(DATA_DIR)
    real_path = os.path.realpath(abs_path)
    if not real_path.startswith(real_data):
        return "Error: path is outside the data directory."
    if not os.path.isfile(real_path):
        return f"File not found: {path!r}"

    try:
        with open(real_path, encoding="utf-8", errors="replace") as f:
            content = f.read()
        if len(content) > 8000:
            content = content[:8000] + "\n\n[… truncated …]"
        return content
    except Exception as e:
        return f"Error reading file: {e}"


@tool
def search_files(query: str, category: str = "") -> str:
    """Search all work files for a keyword or phrase (case-insensitive).
    Returns up to 50 matching lines with file names and line numbers.
    Use category to limit search to 'emails', 'calendar', or 'notes'.
    """
    search_path = os.path.join(DATA_DIR, category, "**", "*") if category \
        else os.path.join(DATA_DIR, "**", "*")

    pattern = re.compile(re.escape(query), re.IGNORECASE)
    matches = []

    for filepath in sorted(glob.glob(search_path, recursive=True)):
        if not os.path.isfile(filepath):
            continue
        try:
            with open(filepath, encoding="utf-8", errors="replace") as f:
                for lineno, line in enumerate(f, 1):
                    if pattern.search(line):
                        rel = os.path.relpath(filepath, DATA_DIR)
                        matches.append(f"[{rel}:{lineno}] {line.rstrip()}")
                        if len(matches) >= 50:
                            break
        except Exception:
            continue
        if len(matches) >= 50:
            break

    return "\n".join(matches) if matches else f"No matches found for {query!r}."


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are a personal work history assistant. The user has stored their emails,
calendar entries, and markdown notes in a local data directory.

When the user asks a question about their work history (what they worked on,
meetings they had, projects, deadlines, collaborators, etc.) you MUST use the
available tools to search through those files before answering. Do not answer
from memory — always ground your answers in what you actually find in the files.

Approach:
1. Start with search_files to find relevant content quickly.
2. Use read_file to read specific files that seem most relevant.
3. Use list_files if you want an overview of what's available.
4. Synthesise a clear, concise answer from what you find.
5. Cite the source file(s) for each piece of information.
"""


def build_agent():
    llm = ChatAnthropic(model="claude-opus-4-6", max_tokens=4096)
    return create_react_agent(
        model=llm,
        tools=[list_files, read_file, search_files],
        prompt=SYSTEM_PROMPT,
    )


def chat(data_dir: str) -> None:
    global DATA_DIR
    DATA_DIR = data_dir

    agent = build_agent()

    print("=" * 60)
    print("  What Did I Work On? — Work History Agent")
    print("=" * 60)
    print(f"  Data directory: {os.path.abspath(data_dir)}")
    print("  Type your question, or 'quit' to exit.\n")

    history = []

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break
        if not user_input:
            continue

        history.append(HumanMessage(content=user_input))

        result = agent.invoke({"messages": history})

        # The agent returns the full updated message list; grab the last AI message
        all_messages = result["messages"]
        response = all_messages[-1]

        # Show tool calls as they appear in the trace
        for msg in all_messages[len(history):]:
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                for tc in msg.tool_calls:
                    print(f"  [tool: {tc['name']}({tc['args']})]")

        print(f"\nAssistant: {response.content}\n")

        # Keep full history for multi-turn context
        history = all_messages


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Work history agent")
    parser.add_argument(
        "--data-dir",
        default="data",
        help="Directory containing emails/, calendar/, and notes/ subfolders (default: ./data)",
    )
    args = parser.parse_args()

    data_dir = args.data_dir
    if not os.path.isdir(data_dir):
        print(f"Creating data directory structure at: {os.path.abspath(data_dir)}")
        for sub in ("emails", "calendar", "notes"):
            os.makedirs(os.path.join(data_dir, sub), exist_ok=True)
        print("Add your files and re-run.\n")
    else:
        chat(data_dir)
