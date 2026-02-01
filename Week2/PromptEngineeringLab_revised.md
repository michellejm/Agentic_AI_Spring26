# Prompt Engineering Lab  
**LLMs and ChatGPT | Spring 2026**  

## Overview

This lab introduces foundational ideas in prompt engineering and uses them to explore a central question for modern AI systems and agentic workflows:

> **What is the relationship between zero-shot prompting, chain-of-thought prompting, and model-side reasoning?**

You will work hands-on with the OpenAI Platform Chat interface to compare how the *same task* behaves under different prompting styles and system settings. Rather than treating prompting as a bag of tricks, this lab emphasizes conceptual understanding: what changes when you add structure versus when the model reasons more internally.

This lab is exploratory rather than prescriptive. There is no single “correct” output. Your goal is to observe patterns, articulate differences, and reflect on how these mechanisms matter for agent design.

---

## Learning Objectives

By the end of this lab, you should be able to:

- Distinguish between **zero-shot**, **few-shot**, and **chain-of-thought-style** prompting
- Explain how **prompt structure** differs from **model-side reasoning effort**
- Use the Platform Chat interface intentionally
- Describe when improvements come from clearer instructions versus increased reasoning
- Connect prompting techniques to early ideas in **agentic AI workflows**

---

## Background: Prompting, Reasoning, and Agents

Large Language Models (LLMs) such as ChatGPT are typically **instruction-tuned**, meaning they are trained to follow user instructions expressed in natural language. Early interactions with these models often relied on *simple prompts*: a single question or instruction, with no examples and no explicit reasoning steps.

Beginning around 2024, models were increasingly tuned for **reasoning**. In this context, *reasoning* means that the model is optimized to internally decompose complex tasks into intermediate steps before producing a final answer.

This lab focuses on how that shift interacts with **prompting strategies**:

- What happens when you provide *no* reasoning structure?
- What happens when you provide *explicit* reasoning structure?
- What happens when the *model itself* is given more reasoning budget?

Understanding these differences is essential for working with **agents**, where models must plan, decide, act, and evaluate—often repeatedly.

---

## Prompting Types

You will encounter (and compare) the following prompting styles:

- **Zero-shot prompting**  
  Asking the model to perform a task without providing examples or a reasoning process.

- **Few-shot prompting**  
  Providing a small number of examples that demonstrate the task before asking the model to perform it.

- **Chain-of-thought-style prompting**  
  Asking the model to articulate an approach or intermediate reasoning steps before producing a final answer.

> Important note: In this lab, “chain of thought” refers to **prompt-visible structure**, not the model’s private internal reasoning.

---

## Core Prompting Principles

As you work through the lab, keep these principles in mind. You will see them echoed in the Platform’s prompt optimizer.

### Be specific  
Ambiguity is almost always interpreted *against* you. Specify:
- The task
- The audience
- The length
- The tone
- Any required components

### Specify the output  
Tell the model *exactly* what the final artifact should look like:
- Paragraph vs. bullets
- Headings or sections
- Required points
- Ordering constraints

### Request *for*, not *against*  
Use affirmative instructions:
- “Write in an academic tone”  
  rather than  
- “Don’t write casually”

### Use “act as if” framing  
Assigning a role can anchor the model’s assumptions and vocabulary.

Example:
> “You are an expert in AI ethics teaching a graduate seminar.”

### Use delimiters  
Structure your prompt visually and logically using markers like:
- `### Instructions`
- `### Context`
- `### Output format`

This reduces confusion and improves consistency.

---

## Tools You Will Use

You may complete this lab using either ChatGPT or Claude. The instructions below assume **ChatGPT**, because I feel that the Platform interface makes system controls more explicit.

### Interfaces

- **ChatGPT (consumer interface)**  
  https://chat.openai.com  
  Useful for quick experimentation, but limited visibility into system controls.

- **OpenAI Platform Chat interface**  
  https://platform.openai.com/chat  
  Allows you to:
  - Select models
  - Adjust reasoning effort
  - Inspect optimized prompts
  - Compare runs more systematically

You will use the **Platform Chat interface** for this lab.

---

## Part 1: Define Your Task (Offline)

Before opening any interface, decide what task you want the model to perform.

### Instructions

Write a short description that answers:

- What do you want the model to do?
- Who is the audience?
- How long should the output be?
- What must it include?

Keep the task **small and readable**. You will be comparing multiple outputs side by side.

### If you need an example task

If you are unsure what to choose, use this:

> Write a short paragraph discussing the ethics of AI agents for a graduate-level audience.

### Constraints for this lab

- Use natural language tasks
- Do not use coding prompts
- Do not use multi-document analysis

The goal is to focus on reasoning and structure, not technical syntax.

### Steps

1. Navigate to the consumer-facing [ChatGPT interface](https://chatgpt.com/). Note the model in the upper left corner.
2. Input your prompt and take note of the output.
3. Make suggestions and modifications until you are satisfied with the output. (keep track of the feedback you give the model)

---

## Part 2: The Platform Chat Interface

In this section, you will run your task through the OpenAI Platform Chat interface and observe how the system treats your prompt.

### Steps

1. Navigate to the [Platform Chat interface:](https://platform.openai.com/chat)

2. Describe your task (or paste the same prompt) into the box below Create a Chat Prompt. Optimize your prompt.

3. Review the optimized prompt in the 'System Message' field.

### Reflection questions (take notes)

After the response, write brief notes addressing:

- How is the optimized prompt structured?
- What information was added?
- Was anything removed or reframed?
- Does the structure suggest chain-of-thought-style reasoning?
- How does this differ from how you originally phrased the task?

These notes will feed directly into your final report.

---
[HERE]


## Part 3: Explore the Fields You Can Modify in the Platform Chat Interface

In this section, you will systematically explore the controls available in the OpenAI **Platform Chat interface**. These controls shape *how* the model responds, independent of *what* you ask it to do.

Your goal is not to master every parameter, but to understand:
- What each control is intended to influence
- When changing a control meaningfully improves results
- When better prompting matters more than system-level changes

---

### Steps
1. Using the 

### A. Model Selection

**What it is**  
The model selector determines which underlying model generates the response.

**Why it matters**  
Different models are optimized for different tradeoffs:
- Speed vs. depth
- General instruction-following vs. explicit reasoning
- Conciseness vs. elaboration

Some models are explicitly tuned to perform additional internal reasoning before producing an answer.

**What to do**
- Run your prompt using one reasoning-oriented model (the o-models) and one general chat model (a mini is a good choice).
- Keep everything else constant.

**Notes to record**
- Which model produced clearer structure?
- Which model followed constraints more reliably?
- Did one model hallucinate or overgeneralize more than the other?

---

### B. Reasoning Effort (or Equivalent Control)

**What it is**  
A control that determines how much internal reasoning the model performs before producing its final answer.

**Why it matters**  
Increasing reasoning effort gives the model more “thinking budget.” This can improve performance on:
- Multi-step reasoning
- Planning and synthesis
- Constraint satisfaction

However, higher reasoning effort can also lead to:
- Longer responses
- Over-explaining
- Diminishing returns for simple tasks

**What to do**
- Run the *same prompt* twice:
  - Once with **low reasoning effort**
  - Once with **high reasoning effort**

**Notes to record**
- Did accuracy improve?
- Did verbosity increase?
- Did the structure improve, or just the length?

> Important: Reasoning effort affects **internal processing**, not whether the model *shows* its reasoning. That is controlled by your prompt.

---

### C. Prompt Optimizer

**What it is**  
A tool that rewrites your prompt according to best practices: clarifying roles, constraints, formatting, and intent.

**Why it matters**  
The optimizer often reveals *implicit assumptions* in your original prompt by making them explicit.

**What to do**
- Compare your original prompt to the optimized version line by line.

**Notes to record**
- What sections were added (e.g., role, task, output format)?
- Were constraints made more explicit?
- Did the optimizer subtly change the task’s meaning?

---

### D. Output Format Controls (When Present)

**What it is**  
Some interfaces allow you to specify or constrain the format of the response.

**Why it matters**  
Structured outputs:
- Are easier to compare across runs
- Reduce ambiguity
- Are critical in agent pipelines

**What to do**
- Enforce a consistent format (e.g., bullets + paragraph) across multiple runs.

**Notes to record**
- Did formatting constraints reduce errors?
- Did the model ever violate the format?

---

### E. Sampling Controls (Temperature, Top-p) (Optional)

**What they are**  
Controls that affect randomness and variability in generation.

**Why they matter**  
- Lower randomness → more consistency
- Higher randomness → more creativity (and sometimes more errors)

**What to do (only if available)**
- Run your prompt with:
  - Low temperature (≈0.2)
  - Higher temperature (≈0.8)

**Notes to record**
- Did creativity increase?
- Did factual accuracy change?
- Was the output still usable?

---

## Part 4: From Zero-Shot to Chain-of-Thought-Style Prompting

In this section, you will evolve *the same task* across three prompting styles.

Keep the **model** and **reasoning effort** constant for all three runs.

---

### Run 1: Zero-Shot Prompt (Baseline)

Use your original prompt from Part 1 with no additional structure.

**Notes to record**
- Did it follow instructions?
- Did it miss key points?
- Was the output coherent and on-topic?

---

### Run 2: Structured Zero-Shot Prompt

Revise your prompt to include explicit constraints, but **no reasoning steps**.

Add:
- Audience
- Length
- Tone
- Required components
- Output format

Example additions:
- Audience: first-year graduate students
- Length: 250–300 words
- Must include: definition, example, counterargument
- Format: bullet points + short conclusion paragraph

**Why this matters**  
This tests whether improvements come from clearer instructions *without* invoking reasoning explicitly.

**Notes to record**
- Did structure improve?
- Did omissions decrease?
- Did the model still make reasoning errors?

---

### Run 3: Chain-of-Thought-*Style* Prompt

Now revise the prompt again to request an explicit *process* before the final output.

Add the following two instructions at the end of your prompt:

1. “Before writing the final answer, write a short plan (3–6 bullet points) describing your approach.”
2. “Then write the final answer in the required format.”

**Notes to record**
- Did the plan improve the final answer?
- Did errors decrease or simply become better explained?
- Was the final output more coherent?

> Reminder: You are testing **visible reasoning structure**, not internal reasoning effort.

---

## Part 5: Reasoning Effort vs. Prompt Structure

Now isolate the role of **model-side reasoning**.

Use your *best prompt* from Part 4 (usually Run 2 or Run 3).

### Runs
- Run A: Low reasoning effort
- Run B: High reasoning effort

Do not change the prompt.

**Notes to record**
- Which version was more accurate?
- Which followed constraints better?
- Which would you trust in an automated agent?

---

## Part 6: Synthesis and Reflection

Answer the following in complete sentences (these will go into your final report):

1. For your task, what mattered more: better prompting or higher reasoning effort? Why?
2. Did explicit planning in the prompt help even when reasoning effort was low?
3. Where did you see diminishing returns?
4. How would your conclusions change for a more complex task?

---

## Optional Extension: Agentic Framing

Take your best-performing prompt and add the following agent-style constraints:

- “Ask up to two clarifying questions if needed.”
- “Produce the output.”
- “Include a self-check section verifying all constraints were met.”

**Reflection**
- How does this resemble an agent loop (plan → act → evaluate)?
- Where might this fail without external tools?

---

## Final Deliverable: User Feedback Report

Email your report to:  
**michellamcsweeney@gmail.com**

### Format
- Google Doc link **or** PDF
- Subject line:  
  **Prompt Engineering Lab — User Feedback Report — Your Name**

### Required Sections

1. Task description (1–2 sentences)  
2. Original zero-shot prompt (paste)  
3. Prompt optimizer observations  
4. Results summary for Runs 1–3  
5. Reasoning effort comparison  
6. Final conclusions  
7. One improvement you would add for deployment in an agent

---

## Closing Note

This lab is not about finding the “best” prompt.

It is about learning to see **where intelligence is coming from**:
- Your instructions
- The model’s reasoning budget
- Or the interaction between the two

That distinction is foundational for understanding—and designing—agentic AI systems.


---

## Submission Instructions

Email your completed **User Feedback Report** to:

**michellamcsweeney@gmail.com**

- Format: Google Doc link **or** PDF
- Subject line:  
  **Prompt Engineering Lab — User Feedback Report — Your Name**

Detailed submission requirements and the report template are provided at the end of the lab.

---

## What to Keep in Mind

This lab is not about finding the “best” prompt.

It is about learning to answer:
- *Why* did this version work better?
- *Where* did the improvement come from?
- *When* should you rely on prompting versus model-side reasoning?

These distinctions are foundational for understanding **agentic AI systems**, where prompting is not a one-time
