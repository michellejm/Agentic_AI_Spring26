# Agentic AI 

Spring 2026 | Wednesdays 6:30-8:30  
CUNY Graduate Center   
Michelle McSweeney | [michelleamcsweeney@gmail.com](mailto:michelleamcsweeney@gmail.com)  
[https://github.com/michellejm/Agentic\_AI\_Spring26](https://github.com/michellejm/Agentic_AI_Spring26) 

### Description

This course explores the emergence of agentic artificial intelligence—AI systems with access to tools that are designed to operate with varying degrees of autonomy in complex, dynamic environments. 

As these systems are rapidly adopted across industries, it marks a fundamental shift from computers-as-tools used by humans to computer programs that ***no longer need human input*** to accomplish tasks. Though there are a wide range of definitions for what constitutes an “agent”, the core idea is centered on autonomy and the ability to direct tasks. As AI evolves from isolated tools into systems capable of independent action (with “agency”), understanding the technical foundations, design constraints, ethical questions, and social risks becomes increasingly vital for shaping agents to mirror the world that we want. By bringing a critical lens to both the technology and its application, the goal of this course is for you to confidently engage with—and shape—the future of agentic AI. You will architect and build an agentic workflow leveraging at least one LLM decision point, and use that experience along with foundational readings to develop an informed, grounded perspective on agentic AI systems and the cultural/social questions they surface. 

This course will be taught using Databricks as the primary development platform though you are welcome to use any LLM orchestration method you prefer. 

### Overview

There are two parts to this course: **technical and social**. These are equally important and the line between them is largely artificial. 

- **The focus of the first half will be technical**. You will design, create, and refine an agent by the midway point of the course. You will explore different low-code and no-code ways of setting them up, and you will gain technical familiarity with how Agents are built.   
- **The focus of second half will be social/humanistic.** You will still keep working on your project, but our attention will shift to considering some of the major debates about the impacts of AI Agents on society and culture. 

**Notes**: 

* LLM-based agents are so new that there is no widely-accepted methodology for how they should be designed and built. There are many methodologies, approaches, and platforms, and by taking this course and engaging in the process, you are shaping these norms.  
* It is entirely possible that something new may come out during this course that completely changes our understanding of how Agents \[should\] work. If that happens, we will learn about it together. 

### LLM Policy

Please use one/some. I don’t care which one, and I don’t expect attribution. To get something decent, you have to do the thinking. To get something well written, you have to do the writing. LLM’s will give you input and are an invaluable tool for working out ideas, phrasing, and organization, but they cannot do the hard work of thinking. That said, they are an *excellent* sounding board and useful tool. Used well, they will make your writing and organization better and clearer. Used poorly and you will simply reiterate trite ideas and language regressed to the mean. It is impossible to form an informed opinion without experience, so you need to use LLMs for some part of your process. However, out of courtesy of our relationship, please do not have an LLM write your emails to me unless you really need help.

### Technology

Labs and examples will be designed with [Databricks free edition](https://www.databricks.com/learn/free-edition) and [Langchain](https://smith.langchain.com). These platforms are **not required.** We are using it because they are great technologies that makes building low-code agents extremely simple. However, if you want to use another platform, you can use anything where you can make an agent. This can be pure python with a Mistral model, crew ai, Anthropic’s Agent Builder, or anything else (don’t worry if you have no idea what any of those things are \- you’ll soon be familiar with the landscape). 

### Project 

You will build an AI agent and evaluate it. This can be an ‘agentic system’, a workflow (there is a distinction, but it’s too academic to be practical), or a multi-agent supervisor. You will have to invent a problem that is sufficiently complex and yet atomizable to justify using an agent. Agents are not the right tool for every problem. Problems will be due very early in the semester as you will need time to work on designing the right flow. 

A good problem for an agent has these properties:

* Requires decision-making under uncertainty (not deterministic)  
* Involves multiple steps, tools, or environments  
* Benefits from autonomy and adaptation  
* Has feedback loops (the agent can learn from results)

Be as creative as you like, or as practical as you like. Some general examples:

* **\[Fill in the blank\] recommender** that processes user input to generate a search query and then either searches the internet for a recommendation or asks for more information.  
* **Research Assistant** that takes a question, performs a focused web or document search, extracts key facts, summarizes them, and responds with sources.\\  
* **Keyword Search Agent** that extracts keywords from \[fill in the blank\] and then does a focused internet search for \[research papers/news articles/etc.\].

Some general but unrealistically ambitious examples. 

* **Continuous competitive intelligence agent** that monitors news, filings, and social signals to alert a company to emerging threats and opportunities.  
* **Personal life-logistics agent** that schedules, reschedules, negotiates conflicts, and optimizes across health, work, and family constraints.  
* **Scientific discovery agent** that proposes hypotheses, designs experiments, evaluates results, and refines future experiments in a closed loop.  
* **Autonomous data analysis agent** that cleans raw datasets, runs exploratory analysis, revises hypotheses, and produces stakeholder-ready reports.  
* **Content creation agent** that reviews input files, searches the internet, summarizes sources, and drafts an essay.

These are very general. Interesting problems tend to be very specific, and the more specific you are, the easier it will be to set up a constrained workflow. We will work on this together – there are two 1:1 sessions to discuss your project via Zoom. 

Projects will be due at the end of the semester. We will have a “poster session” style presentation to showcase projects on the last day. 

Projects have three pieces:

1. A proposal (30%). Proposals should include:  
   1. A problem statement  
      1. A clear description of the problem or task your agent is intended to address.  
      2. An explanation of why this problem justifies an *agentic* approach (as opposed to a script, chatbot, or single model call).  
   2. A proposed design, indicating  
      1. The decision points, including:  
         1. What decision is being made at each point (e.g., planning, routing, evaluation, delegation).  
         2. Whether the decision is deterministic or non-deterministic  
      2. Explanation of tool use  
         1. What tools can be called at each decision point.  
         2. Why those tools  
      3. Feasibility analysis   
         1. Evidence that the project is technically achievable within the course timeline (propose what tools you will use)  
         2. Clear articulation of scope: what you *will* build and what you are intentionally leaving out.  
2. The technical artifact (20%)  
   1. The technical implementation (AI should help you with this)  
   2. The decision points working  
   3. A result or output that is generated  
   4. The final presentation  
3. A reflection (50%)  
   1. Description of the design, goal, and decision points  
      1. Clear explanation of your agent’s goal, structure, and decision points.  
      2. Description of the decisions you made along the way.  
      3. Reflection on design tradeoffs and limitations.  
   2. Social/cultural/humantistic evaluation.   
      1. Situate your agent within a larger social or cultural context  
      2. Consider implications at:  
         1. An individual level (e.g., cognition, responsibility, dependency), and/or  
         2. A societal or scale level (e.g., labor, institutions, power, norms)  
      3. Ground your analysis in:  
         1. Course readings,  
         2. Historical or philosophical discussions of agency, or  
         3. Contemporary debates around AI and autonomy.  
   3. Your own review of your agent  
      1. Your assessment of:  
         1. The agent’s usefulness or effectiveness,  
         2. Whether it achieved its stated goals,  
         3. Its significance as a symbol or example of broader agentic trends.  
      2. This evaluation should be grounded in a broader context, not purely personal opinion.

Strong projects will:

* Use agents intentionally to solve a complex problem  
* Leverage decision making and articulate the decisions clearly  
* Show awareness that agentic systems (and all technologies) are not just tools, but are situated in social systems and their presence affects the system.  
* Treat agents as objects of reflection, not just optimization.

### Labs

Labs are given \~weekly. They will be graded on completion and are worth 25% of your grade. Some are more technical than others. Submit them via email. If you can’t get one to work, explain what your set up is, what the problem is, and what you tried. You can do this in writing or a screen recording video. You need to either get it to work or clearly explain your steps in a way that I could reproduce the problem and troubleshoot it.

### Agenda

The readings/lab should be completed before the class session they are listed for. 

| W  | Date      | Topic                                  | Readings | Due |
|----|----------|----------------------------------------|----------|-----|
| 1  | 1/28     | Introduction | (optional) [Intelligent Agents: Theory and Practice](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated1/woodridge_intelligent_agents.pdf) – Wooldridge & Jennings, 1995 <br> (optional) [Agency – Sections 1 & 2](https://plato.stanford.edu/archives/win2019/entries/agency/#ConTheKinAge) (Stanford Encyclopedia of Philosophy) | Sign up for [Databricks Free Edition](https://login.databricks.com/signup?dbx_source=docs&intent=SIGN_UP) and [Langsmith](https://smith.langchain.com/) (free) |
| 2  | 2/4      | Brief intro to LLMs |  | [Single Tool Agent Lab](https://github.com/michellejm/Agentic_AI_Spring26/tree/main/Week1) |
| 3  | 2/11     | Defining Agents, Agent Taxonomy, Tools and Tool Calling | [Building Effective Agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents)** <br> [Huggingface: What is an Agent](https://huggingface.co/docs/smolagents/en/conceptual_guides/intro_agents) <br> (optional) [AI Agents vs. Agentic AI](https://arxiv.org/abs/2505.10468) <br> (optional) [OpenAI on Tools](https://platform.openai.com/docs/guides/function-calling) | [Prompt Engineering Lab](https://github.com/michellejm/Agentic_AI_Spring26/blob/main/Week2_LLMs/PromptEngineeringLab_revised.md) |
| 4  | 2/18     | MCP, Problems for Agents, Designing an Agentic System | [MCP Introduction](https://www.anthropic.com/news/model-context-protocol) <br> (optional) [Databricks MCP Docs](https://docs.databricks.com/aws/en/generative-ai/mcp/) | [Reasoning Mini-Lab](https://github.com/michellejm/Agentic_AI_Spring26/blob/main/Week3_ReAct/Prompting_mini_lab.md) and PB&J Lab |
| 5  | 2/25     | Problems for Agents, Designing an Agentic System | [Practical Guide for Production-Grade Agentic AI Workflows](https://arxiv.org/abs/2512.08769) (Section 3 only)** <br> [Designing a Successful Agentic AI System](https://hbr.org/2025/10/designing-a-successful-agentic-ai-system) (HBR – library access) | [Goodreads Lab](https://github.com/michellejm/Agentic_AI_Spring26/tree/main/Week4_MCP) |
| 6  | 3/4      | Context, Memory, and Learning | [Architecting Efficient Context-Aware Multi-Agent Framework](https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/) <br> (optional) [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) <br> [How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system) <br> [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) | **Problem Statement** + [Multi-Agent Lab](https://github.com/michellejm/Agentic_AI_Spring26/blob/main/Week5_Design-Context/lab_instructions.md) |
| 7  | 3/11     | Project Design Review (Zoom) | 1:1 project meetings | **Project Design** (due 8pm on 3/10) |
| 8  | 3/18     | Agent Evaluation and Governance | [Best Practices for Agentic Benchmarks](https://arxiv.org/abs/2507.02825) <br> [Survey on LLM-as-Judge](https://arxiv.org/abs/2411.15594) <br> [LLM-as-a-Judge Explained](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method) <br> [Agentic AI: Comparing Open-Source Frameworks](https://medium.com/data-science-collective/agentic-ai-comparing-new-open-source-frameworks-21ec676732df) <br> (optional) [LangChain Quickstart](https://docs.langchain.com/oss/python/langchain/quickstart) <br> (optional) [DSPy Docs](https://dspy.ai/) <br> [AI Agents in Action (WEF)](https://www.weforum.org/publications/ai-agents-in-action-foundations-for-evaluation-and-governance/) | RLHF Lab |
| X  | SKIP     | Agency Since 1950 | *Pick one:* <br> (a) [Newell & Simon on Symbolic AI](https://philarchive.org/rec/AUGFST-2) <br> (b) [Could Symbolic AI Unlock Human-Like Intelligence?](https://www.scientificamerican.com/article/could-symbolic-ai-unlock-human-like-intelligence/) <br> (c) McCarthy – Programs with Common Sense <br> (d) Minsky & Papert – Society of Mind <br> (optional) [ReAct Paper](https://arxiv.org/abs/2210.03629) <br> [Self-Prompting LLMs](https://arxiv.org/abs/2212.08635) <br> [Fully Autonomous AI Agents Should Not Be Developed](https://arxiv.org/pdf/2502.02649) | NA |
| 9  | 3/25     | Agents as Workers / Teams (Trust) | [Steam, Steel, and Infinite Minds](https://www.notion.com/blog/steam-steel-and-infinite-minds-ai) <br> [How Do AI Agents Do Human Work?](https://arxiv.org/html/2510.22780v1) <br> [Future of Work with AI Agents](https://arxiv.org/abs/2506.06576)** | Eval Lab |
| —  | 4/1      | No Class |  |  |
| —  | 4/8      | No Class |  |  |
| 10 | 4/15     | AI Anthropomorphism / Human-Agent Relationships / Agents in Education | Selected readings (TBD by vote) | TBD |
| 11 | 4/22     | Project Consultations (Zoom) |  | **Project Prototype** |
| 12 | 4/29     | Agents as Thinking Machines | (optional) [Turing (1950)](https://phil415.pbworks.com/f/TuringComputing.pdf) <br> [Reasoning in LLM-based Agents](https://arxiv.org/abs/2503.11074) <br> [What is a Reasoning Model?](https://www.ibm.com/think/topics/reasoning-model)** | Work on Projects |
| 13 | 5/6      | Agents and Personhood | (optional) [Frankfurt (1971)](https://www-jstor-org.ezproxy.gc.cuny.edu/stable/2024717) <br> [Anthropomorphic Conversational Agents](https://www.pnas.org/doi/10.1073/pnas.2415898122)** <br> [Theory of AI Personhood](https://arxiv.org/abs/2501.13533v1) <br> [Artificial Agents – Personhood in Law](https://www.sci.brooklyn.cuny.edu/~schopra/agentlawsub.pdf) | Work on Projects |
| 14 | 5/13     | Presentations |  |  |

\*\* Most essential readings

Supplemental Readings (I will keep adding to this list):

- Russel and Norvig (2020). [Artificial Intelligence: a modern approach](https://people.engr.tamu.edu/guni/csce625/slides/AI.pdf).
