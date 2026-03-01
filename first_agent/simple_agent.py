import json
from langchain.agents import create_agent
from dataclasses import dataclass
from langchain.agents.structured_output import ToolStrategy

@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    # A agent response (always required)
    agent_response: str

print('Creating Agent')

agent = create_agent(
    "google_genai:gemini-2.5-flash", 
    system_prompt="You are a helpful assistant. Be concise and accurate.",
    response_format=ToolStrategy(ResponseFormat),
    )
print('Agent Created')

print('Invoking Agent')
results = agent.invoke(
    {"messages": [{"role": "user", "content": "Explain machine learning"}]},
    context={"user_role": "expert"},
    
)
print("Results:")
