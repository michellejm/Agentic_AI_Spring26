# Vibe Coding Lab

**Practical Considerations for AI Agent Design | Spring 2026**

---

## Objective

* Experience "vibe coding" — use an LLM to write functional code through iterative prompting, **without writing the code yourself**.
* Build a word-frequency visualization from a text of your choice (or pick another project).
* Develop a record of your prompting decisions and reasoning.

---

## Deliverable

Two things:

1. **A working visualization** — a word-frequency chart or plot generated from a text you chose.
2. **A prompt diary** — a running log of every prompt you gave the LLM, why you gave it, and what changed. This is the more important artifact. The log is evidence of your thinking.

Submit both via email.

---

## Background

"Vibe coding" refers to directing a model to write code for you through natural language — iterating on prompts until the output does what you want, without writing the code yourself. This is increasingly how non-engineers (and many engineers) interact with code in agentic systems.

Word-frequency visualization is a classic task in digital humanities and text analysis: take a body of text, count how often each word appears, and display the results. It's a small enough task to finish in one session, but it has real extension paths if you want to go further.

---

## The Prompt Diary

Before you start coding, open a document (Google Doc, notes app, whatever) and keep it open the whole time. For every prompt you give the LLM, log:

- The prompt you sent
- What the LLM returned
- What you decided to do next and **why**

The diary is not a transcript — it's your reasoning. If you changed direction, say why. If something surprised you, note it.

---

## Steps

### Part 1: Choose Your Text

1. Pick a text you find interesting — a novel, a speech, a dataset of tweets, lyrics, anything.
2. If you need a starting point, use a public domain text from [Project Gutenberg](https://www.gutenberg.org/).
3. Save it as a plain `.txt` file.

### Part 2: Set Up Your Environment

Choose one:

**Option A — Databricks**
- Open a new notebook in your Databricks workspace.
- Upload your `.txt` file to the same folder.

**Option B — Local / Colab**
- Open [Google Colab](https://colab.research.google.com/) or a local Jupyter notebook.
- Upload your `.txt` file or provide a path to it.

### Part 3: Vibe Code the Visualization

1. Open your LLM of choice (Claude, ChatGPT, Gemini, etc.).
2. Start your prompt diary.
3. Ask the LLM to write code that:
   - Reads your text file
   - Counts word frequencies
   - Displays the top N most frequent words as a chart
4. Copy the generated code into your notebook and run it.
5. Iterate — if it doesn't work, or doesn't look how you want, prompt again. Log every exchange.

**Do not write any code yourself.** Your only job is to direct the LLM through prompts.

### Part 4: Refine

Once the basic visualization works, try at least one of the following through prompting:

- Remove common stopwords (e.g., "the", "and", "a") and regenerate
- Change the chart type (bar chart → word cloud, or vice versa)
- Adjust the number of words displayed

Log every change and your reasoning for making it.

---

## Extension Challenges (Optional)

If you finish early or want to go further:

- **Compare two texts** — modify the code to display word frequencies side by side
- **Filter by part of speech** — prompt the LLM to add POS tagging and show only nouns or verbs
- **Track frequency across chapters** — if your text has chapters, plot how a key word's frequency changes across them
- **Add tf-idf** — instead of raw frequency, prompt for a tf-idf score to surface more distinctive words

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
