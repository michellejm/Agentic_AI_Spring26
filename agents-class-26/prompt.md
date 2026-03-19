Create an explanation application. 

1. On the screen, there should be 2 panels. On the left panel is a diagram showing the agent flow with boxes for each step. On the right is the code. 
2. Use the code for the agent in this folder @agent.py
3. A user can hover on a box in the digram and it will highlight the block of code that is responsible for that step
4. If a user clicks on a line of code, they see a popup explaining what it is responsible for. For example: 'from langchain_anthropic import ChatAnthropic' : "Imports the ChatAnthropic class from the langchain-anthropic package — which is the official LangChain integration for Claude. It lets you use Claude as the LLM inside any LangChain chain or agent"