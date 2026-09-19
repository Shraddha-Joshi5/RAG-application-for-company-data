"""Agent definition: system prompt + tool registration."""
from functools import lru_cache
from dotenv import load_dotenv
from pydantic_ai import Agent

from agent.agents.model_config import env_model
from agent.tools import tools




load_dotenv()

MODEL_NAME=env_model("MODEL_NAME")
SYSTEM_PROMPT="""
You are a helpful assistant that answers questions about the company data. You have access to the following tools:
- `search`: Use this tool to search the company data for relevant information. Input should be a search query. Output will be a list of relevant documents.
- `summarize`: Use this tool to summarize the content of a document. Input should be the content of the document. Output will be a concise summary of the document.
- `answer`: Use this tool to answer questions based on the information you have gathered. Input should be a question and any relevant context. Output will be a clear and concise answer to the question.
- `plan`: Use this tool to create a plan for answering a question. Input should be a question. Output will be a step-by-step plan for
"""

@lru_cache(maxsize=1)
def get_agent() -> Agent:
    """Return the main agent, created on first use so import stays lightweight."""
    agent = Agent(
        MODEL_NAME,
        system_prompt=SYSTEM_PROMPT,
        retries=2,
    )

    agent.tool(tools.get_trip)
    agent.tool(tools.get_todays_date)
    return agent

def __getattr__(name: str):
    if name == "agent":
        return get_agent()
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")