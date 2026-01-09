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
- **The focus of second half will be social/humanistic.** You will still keep working on your project, but our attention will shift to considering some of the major debates about the social and humanistic impacts of AI Agents on society and culture. 

**Notes**: 

* LLM-based agents are so new that there is no widely-accepted methodology for how they should be designed and built. There are many methodologies, approaches, and platforms, and by taking this course and engaging in the process, you are shaping these norms.  
* It is entirely possible that something new may come out during this course that completely changes our understanding of how Agents \[should\] work. If that happens, we will learn about it together. 

### LLM Policy

Please use one/some. I don’t care which one, and I don’t expect attribution. To get something decent, you have to do the thinking. To get something well written, you have to do the writing. LLM’s will give you input and are an invaluable tool for working out ideas, phrasing, and organization, but they cannot do the hard work of thinking. That said, they are an *excellent* sounding board and useful tool. Used well, they will make your writing and organization better and clearer. Used poorly and you will simply reiterate trite ideas and language regressed to the mean. It is impossible to form an informed opinion without experience, so you need to use LLMs for some part of your process. However, out of courtesy of our relationship, please do not have an LLM write your emails to me unless you really need help.

### Technology

Labs and examples will be designed with [Databricks free edition](https://login.databricks.com/signup?provider=DB&scid=7018Y000001Fi0MQAS&utm_medium=paid+search&utm_source=google&utm_campaign=14272820537&utm_adgroup=126939742998&utm_content=trial&utm_offer=trial&utm_ad=724888424298&utm_term=try+databricks&dbx_source=paid&gad_source=1&gad_campaignid=14272820537&gbraid=0AAAAABYBeAgN8faJvyztx6K3zkLs-x-LR&gclid=Cj0KCQiAgbnKBhDgARIsAGCDdlczQLkq1VO9_gifhMg4ECRalE2jpvKaydrxjKX4aVu9CUC8s60urzYaAggzEALw_wcB&tuuid=c06da659-c6bd-4b92-b597-7cb5c09e1fd8&intent=SIGN_UP&rl_aid=62958b3c-5a57-4fb3-bd5a-0ac49f32b132&sisu_state=eyJsZWdhbFRleHRTZWVuIjp7Ii9zaWdudXAiOnsidG9zIjp0cnVlLCJwcml2YWN5Ijp0cnVlLCJjb3Jwb3JhdGVFbWFpbFNoYXJpbmciOnRydWV9fX0%3D) and [Langchain](https://smith.langchain.com/o/c7a3c136-90c0-4334-98e9-f4e7cad53f5b). These platforms are **not required.** We are using it because they are great technologies that makes building low-code agents extremely simple. I also work at Databricks and can therefore support you in it. However, if you want to use another platform, you can use anything where you can make an agent. This can be pure python with a Mistral model, Langchain, Anthropic’s Agent Builder, or anything else (don’t worry if you have no idea what any of those things are \- you’ll soon be familiar with the landscape). You can use some of these within Databricks, so it’s really not an ‘either/or’ situation. 

### Project 

You will build an AI agent and evaluate it. This can be an ‘agentic system’, a workflow (there is a distinction, but it’s too academic to be practical), or a multi-agent supervisor. You will have to invent a problem that is sufficiently atomic to justify using an agent. Agents are not the right tool for every problem. Problems will be due very early in the semester as you will need time to work on designing the right flow. 

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

| W | Date | Topic | Readings | Due |
| :---- | :---- | :---- | :---- | :---- |
| 1 | 1/28 | Introduction,  Defining Agents, Agent Taxonomy, Orientation to Databricks Free | (optional) [Intelligent Agents: Theory and Practice](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated1/woodridge_intelligent_agents.pdf) \- Wooldridge & Jennings, 1995 (optional) [Agency \- Sections 1 & 2](https://plato.stanford.edu/archives/win2019/entries/agency/#ConTheKinAge) (Stanford Encyclopedia of Philosophy) | Sign up for [Databricks Free Edition](https://login.databricks.com/signup?dbx_source=docs&intent=SIGN_UP&tuuid=5c7e20d4-efca-4207-a49a-7ffaaf35ab45&rl_aid=62958b3c-5a57-4fb3-bd5a-0ac49f32b132&provider=DB_FREE_TIER&sisu_state=eyJsZWdhbFRleHRTZWVuIjp7Ii9zaWdudXAiOnsidG9zIjp0cnVlLCJwcml2YWN5Ijp0cnVlLCJjb3Jwb3JhdGVFbWFpbFNoYXJpbmciOnRydWV9fX0%3D) and [Langsmith](https://smith.langchain.com/) (free) |
| 2 | 2/4 | Problems for Agents;  Tools and Tool Calling, MCP | [Building Effective Agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents) \*\* (optional) [OpenAI on Tools](https://platform.openai.com/docs/guides/function-calling) [Huggingface What is an Agent](https://huggingface.co/docs/smolagents/en/conceptual_guides/intro_agents) (optional) [AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges](https://arxiv.org/abs/2505.10468) [MCP Architecture](https://modelcontextprotocol.io/docs/learn/architecture) (optional) [Databricks MCP docs](https://docs.databricks.com/aws/en/generative-ai/mcp/)  | Single tool Agent Lab |
| 3 | 2/11 | Designing an Agentic System | [A Practical Guide for Designing, Developing, and Deploying Production-Grade Agentic AI Workflows](https://arxiv.org/abs/2512.08769) (section 3 only, rest is optional)\*\* [Designing a Successful Agentic AI System](https://hbr.org/2025/10/designing-a-successful-agentic-ai-system) (HBR- available via library)   | Multiple tool Agent Lab |
| 4 | 2/18 | Agent Evaluation | [Establishing Best Practices for Building Rigorous Agentic Benchmarks](https://arxiv.org/abs/2507.02825) [A Survey on LLM-as-judge](https://arxiv.org/abs/2411.15594) [LLM-as-a-Judge Simply Explained: The Complete Guide to Run LLM Evals at Scale](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method)   | Evaluation Lab |
| 5 | 2/25 | Frameworks (Langchain, DsPy), and governance |  [Agentic AI: Comparing New Open-Source Frameworks](https://medium.com/data-science-collective/agentic-ai-comparing-new-open-source-frameworks-21ec676732df) [Langchain quickstart](https://docs.langchain.com/oss/python/langchain/quickstart) (optional) [DSPy docs](https://dspy.ai/) [AI Agents in Action: Foundations for Evaluation and Governance](https://www.weforum.org/publications/ai-agents-in-action-foundations-for-evaluation-and-governance/)  | Langchain lab |
| 6 | 3/4 | Context, memory, and learning/self-improvement | [Architecting efficient context-aware multi-agent framework for production](https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/) (optional) [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427)  [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228)   |  Context window lab **Problem Statement**  |
| 7 | 3/11 | Project Design Review ZOOM | 1:1 project meetings   | **Project Design** (due 8pm on 3/10) |
| 8 | 3/18 | Agency since 1950  | *Pick one from (a) to (d)* (a) [From Symbols to Knowledge Systems: A. Newell and H. A. Simon’s Contribution to Symbolic AI](https://philarchive.org/rec/AUGFST-2) (b) [Could Symbolic AI Unlock Human-Like Intelligence?](https://www.scientificamerican.com/article/could-symbolic-ai-unlock-human-like-intelligence/) (c) McCarthy’s Programs with Common Sense \[[tk](https://www.sciencedirect.com/science/article/pii/S0004370210001827#:~:text=Introduction%20This%20special%20issue%20is,specified%20declaratively%20to%20the%20program.)\] (d) Minsky and Papert Microworlds and Society of Mind \[tk\] [ReAct: Synergizing Reasoning and Acting in Language Modes](https://arxiv.org/abs/2210.03629) *(optional)* [Self-Prompting Large Language Models for Zero-Shot Open-Domain QA](https://arxiv.org/abs/2212.08635) [Fully Autonomous AI Agents Should Not Be Developed](https://arxiv.org/pdf/2502.02649) | Prompt Engineering lab |
| 9 | 3/25 | Agents as workers/teams (trust) | [Steam, Steel, and Infinite Minds](https://www.notion.com/blog/steam-steel-and-infinite-minds-ai) [How Do AI Agents Do Human Work? Comparing AI and Human Workflows Across Diverse Occupations](https://arxiv.org/html/2510.22780v1) [Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce](https://arxiv.org/abs/2506.06576)\*\*  | Build a team lab |
|  | 4/1, 4/8 |  |  |  |
| 10 | 4/15 | \[CLASS CHOICE\] AI anthropomorphism ([1](https://arxiv.org/abs/2402.02056), [2](https://www.nngroup.com/articles/anthropomorphism/), 3\) Human-agent relationships ([1](https://arxiv.org/abs/2506.12605), [2](https://www.nature.com/articles/s44387-025-00041-7), [3](https://ojs.aaai.org/index.php/AIES/article/view/31694)) Agents in education (1, 2, 3\) etc. | *This week will be somewhere along the continuum of how we have anthropomorphised AI agents. We will take a simple vote if this will be general or specific.* |  |
| 11 | 4/22 | Project Consultations  ZOOM |  | **Project prototype** |
| 12 | 4/29 | Agents as thinking machines | *(optional*) [Computing Machinery and Intelligence](https://phil415.pbworks.com/f/TuringComputing.pdf) \- Turing, 1950 [Exploring the Necessity of Reasoning in LLM-based Agent Scenarios](https://arxiv.org/abs/2503.11074) [What is a reasoning model?](https://www.ibm.com/think/topics/reasoning-model)\*\* | Reasoning lab |
| 13 | 5/6 | Agents and personhood | (optional) [Freedom of Will and Concept of a Person](https://www-jstor-org.ezproxy.gc.cuny.edu/stable/2024717), [Frankfurt, 1971](https://www-jstor-org.ezproxy.gc.cuny.edu/stable/2024717) (available via library)  [The benefits and dangers of anthropomorphic conversational agents](https://www.pnas.org/doi/10.1073/pnas.2415898122)\*\* [Towards a Theory of AI Personhood](https://arxiv.org/abs/2501.13533v1) [Artificial Agents \- Personhood in Law and Philosophy](https://www.sci.brooklyn.cuny.edu/~schopra/agentlawsub.pdf)  (optional) [Intentionality, Agency and Personhood: Outline of a Phenomenological Theory of Acts](https://www-jstor-org.ezproxy.gc.cuny.edu/stable/27118151?seq=1) | PB\&J lab |
| 14 | 5/13 | Presentations  |  |  |

\*\* Most essential readings

Supplemental Readings (I will keep adding to this list):

- Russel and Norvig (2020). [Artificial Intelligence: a modern approach](https://people.engr.tamu.edu/guni/csce625/slides/AI.pdf).
