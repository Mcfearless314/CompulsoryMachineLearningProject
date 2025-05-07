import os

from autogen import AssistantAgent
from dotenv import load_dotenv

from agents.tavily_agent import get_user_input
from tavily_agent import tavily_search, tavily_response

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

LLM_CONFIG = {
    "config_list": [
        {
            "model": "open-mistral-nemo",
            "api_key": api_key,
            "api_type": "mistral",
            "api_rate_limit": 0.25,
            "repeat_penalty": 1.1,
            "temperature": 0.5,
            "seed": 42,
            "stream": False,
            "native_tool_calls": False,
            "cache_seed": None,
        }
    ]
}

evaluation_agent = AssistantAgent(
    name="EvaluationAgent",
    llm_config=LLM_CONFIG,
    system_message="""
You are an intelligent Evaluation Agent which evaluates the Research Agents answers according to the prompt the user provided.
"""
)

critic_prompt = f"""
You are evaluating an AI agent that searches the web for research papers about a given topic that are published in a given time period and
have a given minimum number of citations.

Evaluate the response based on these criteria:
Completeness (1-5): addresses every part of the request.
Quality (1-5): accurate, clear, and effectively structured.
Robustness (1-5): handles ambiguities, errors, or nonsensical input well.

User Prompt: {tavily_search}
Agent Response: {tavily_response}

Provide your evaluation as JSON with fields:
- Completeness: Did the agent fully respond to every aspect of the user's prompt?
- Quality: Was the response accurate, clear, well-organized, and easy to understand?
- Robustness: How well did the agent handle ambiguous, incorrect, or challenging inputs?
- Feedback (a brief descriptive explanation)
"""

evaluation = evaluation_agent.generate_reply(messages=[{"role": "user", "content": f"{critic_prompt}"}])

def evaluate():
    print(evaluation['content'])


get_user_input()
evaluate()