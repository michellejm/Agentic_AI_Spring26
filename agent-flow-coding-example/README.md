# Agent Flow Coding Example

This folder contains a working example of a LangChain/LangGraph ReAct agent, paired with an interactive visualization of how it works. It was built using vibe coding — the agent and the UI were both generated through iterative prompting, not written by hand.

## Files

### `agent.py`
A command-line agent called **"What Did I Work On?"** It scans a local folder of emails, calendar entries, and markdown notes, then answers natural-language questions about your work history. Built with LangChain and LangGraph's `create_react_agent`, using Claude as the underlying model.

The agent has three tools:
- `list_files` — browse available files by category (emails, calendar, notes)
- `read_file` — read the full contents of a specific file
- `search_files` — keyword search across all files

Run it with:
```bash
export ANTHROPIC_API_KEY=your_key_here
python agent.py --data-dir data
```

### `index.html`
An interactive, browser-based visualization of the agent's flow. Open this file directly in a browser (no server needed). It shows:
- **Left panel**: a diagram of the agent's steps and decision points
- **Right panel**: the actual code from `agent.py`

Hover over a box in the diagram to highlight the corresponding block of code. Click a line of code to see a plain-English explanation of what it does.

### `diagram.md`
A Mermaid flowchart showing the agent's architecture — from user input through message history, the ReAct loop, tool calls, and back to the final answer. The same structure is rendered interactively in `index.html`.

### `prompt.md`
The prompt used to generate `index.html`. Included so you can see exactly what instruction produced the interactive visualization — a demonstration of what a well-scoped vibe coding prompt looks like.

### `data/`
An empty placeholder directory with three subdirectories: `emails/`, `calendar/`, and `notes/`. Drop your own `.txt`, `.md`, or `.eml` files here before running the agent.

### `.gitignore`
Prevents actual personal data files from being accidentally committed.
