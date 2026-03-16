# Vibe Coding Lab

**Practical Considerations for AI Agent Design | Spring 2026**

---

## Objective

* Experience "vibe coding" — use an LLM to write functional code through iterative prompting, **without writing the code yourself**.
* Build a working program from a text or data source of your choice.
* Develop a record of your prompting decisions and reasoning.

---

## Deliverable

Two things:

1. **A working program** — a completed, running artifact (visualization, script, or app) generated from the task you chose.
2. **A prompt diary** — a running log of every prompt you gave the LLM, why you gave it, and what changed. This is the more important artifact. The log is evidence of your thinking.

Submit both via email.

---

## Background

"Vibe coding" refers to directing a model to write code for you through natural language — iterating on prompts until the output does what you want, without writing the code yourself. This is increasingly how non-engineers (and many engineers) interact with code in agentic systems.

This lab offers two task tracks depending on your comfort level. Both are legitimate — the goal is the prompting practice, not the complexity of the output.

---

## The Prompt Diary

Before you start coding, open a document (Google Doc, notes app, whatever) and keep it open the whole time. For every prompt you give the LLM, log:

- The prompt you sent
- What the LLM returned
- What you decided to do next and **why**

The diary is not a transcript — it's your reasoning. If you changed direction, say why. If something surprised you, note it.

---

## Steps

### Part 1: Choose Your Task Track

**Track A — Word-Frequency Visualization** *(accessible)*

A classic digital humanities task: take a body of text, count how often each word appears, and display the results as a chart. Small enough to finish in one session, with natural extension paths.

1. Pick a text you find interesting — a novel, a speech, a dataset of tweets, lyrics, anything.
2. If you need a starting point, use a public domain text from [Project Gutenberg](https://www.gutenberg.org/).
3. Save it as a plain `.txt` file.

---

**Track B — Simple Data Dashboard** *(more challenging)*

Build a multi-panel interactive dashboard from a structured dataset. This is harder because it requires the LLM to coordinate multiple components (data loading, filtering, layout, interactivity) and you will need to debug across them.

1. Find or download a CSV dataset you're curious about. Some starting points:
   - [NYC Open Data](https://opendata.cityofnewyork.us/)
   - [Kaggle Datasets](https://www.kaggle.com/datasets) (free account required)
   - [Our World in Data](https://ourworldindata.org/)
2. Your dashboard should include at least:
   - Two different chart types (e.g., bar chart + line chart)
   - A filter or dropdown that updates the charts
   - A title and basic labels

The challenge is managing the back-and-forth with the LLM as complexity grows. Pay attention to when it loses track of earlier context and how you recover.

---

### Part 2: Set Up Your Environment

**If you have a subscription to Claude, ChatGPT, or Google:**

Use the CLI tool directly in your terminal — this is closer to how developers actually vibe code and gives you a better feel for the agentic workflow.

- **[Claude Code](https://docs.anthropic.com/en/docs/claude-code)** (requires Claude subscription) — runs in your terminal, can read and write files directly
- **[Codex CLI](https://github.com/openai/codex)** (requires ChatGPT Plus or API access) — OpenAI's terminal-based coding agent
- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** (requires Google account) — Google's terminal coding agent

**If you do not have a subscription:**

Use [Cursor](https://www.cursor.com/) — a code editor with a built-in AI assistant. The free tier is sufficient for this lab.

1. Download and install Cursor.
2. Open a new folder as your project directory.
3. Use the chat panel to direct it — you do not need to type in the code editor yourself.

**Notebook fallback (always works):**
- [Google Colab](https://colab.research.google.com/) with any chat-based LLM open alongside it
- Databricks notebook (upload your data file to the same folder)

### Part 3: Vibe Code

1. Start your prompt diary.
2. Give the LLM your first prompt describing what you want to build.
3. Run the code it produces.
4. Iterate — if it doesn't work, or doesn't look right, prompt again. Log every exchange.

**Do not write any code yourself.** Your only job is to direct the LLM through prompts.

### Part 4: Refine

Once the basic version works, push it further through prompting. For Track A, try at least one of:

- Remove common stopwords (e.g., "the", "and", "a") and regenerate
- Change the chart type (bar chart → word cloud, or vice versa)
- Adjust the number of words displayed

For Track B, try at least one of:

- Add a second filter (e.g., by date range or category)
- Change the color scheme or layout based on your feedback
- Export the chart as an image or the filtered data as a CSV

Log every change and your reasoning for making it.

---

## Extension Challenges (Optional)

If you finish early or want to go further:

*Track A:*
- **Compare two texts** — modify the code to display word frequencies side by side
- **Filter by part of speech** — prompt the LLM to add POS tagging and show only nouns or verbs
- **Track frequency across chapters** — if your text has chapters, plot how a key word's frequency changes across them
- **Add tf-idf** — instead of raw frequency, prompt for a tf-idf score to surface more distinctive words

*Track B:*
- **Add a summary statistics panel** — prompt for a stats table alongside the charts
- **Make it shareable** — ask the LLM to package the dashboard as a standalone HTML file
- **Connect a second dataset** — merge in a related CSV and prompt for a combined view

---

## Reflection Questions

Answer these in writing (a few sentences each) as part of your submission:

1. What was your first prompt, and what did you have to change about it to get useful output?
2. Where in the process did you feel most in control? Where did you feel least in control?
3. **What is the difference between writing code and directing someone (or something) to write it for you?** Is there a meaningful distinction — and does it matter for the quality of the result?
4. How does this experience connect to how agents operate? What parts of what you did resemble what an agent does?

---

## Submission

Email your prompt diary and a screenshot or export of your visualization to:
michelleamcsweeney@gmail.com
