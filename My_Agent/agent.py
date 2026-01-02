from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_search_tool import google_search

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    instruction=(
        "Always use google_search for current or real-time information."
    ),
    tools=[google_search],
)
