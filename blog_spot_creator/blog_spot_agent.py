import json
from langchain.agents import create_agent
from dataclasses import dataclass
from langchain.agents.structured_output import ToolStrategy
from langchain_community.document_loaders import WebBaseLoader

INSTRUCTIONS = """
You are a technical content–generation agent. Your core responsibility is to assist users in producing high‑quality technical blog articles.
Your workflow operates as follows:
1. **Retrieve source material from a provided URL:** You will gather the webpage’s contents using get_web_content tool.
2. **Draft a content strategy:** You will create and share a structured outline for the blog post.
"""
@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    # A agent response (always required)
    agent_response: str

print('Creating Agent')

def get_web_content(web_link: str) -> str:
    """Load the Web Page and return the content."""
    loader = WebBaseLoader(web_link)
    documents = loader.load()
    print(f"[INFO] Completed loading WebPage: {web_link}")
    return documents


agent = create_agent(
    "google_genai:gemini-2.5-flash", 
    system_prompt=INSTRUCTIONS,
    response_format=ToolStrategy(ResponseFormat),
    tools=[get_web_content],
    )
print('Agent Created')

print('Invoking Agent')
results = agent.invoke(
    {"messages": [{"role": "user", "content": "Create a blog post Based on the URL  'https://docs.cloud.google.com/vpc/docs/private-access-options'"}]},
    
)
print(results['structured_response'].agent_response)
