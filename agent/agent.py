from langchain.agents import create_agent
from agent.tools import describe_file, query_file
from agent.prompt import SYSTEM_PROMPT
from langchain_google_genai import ChatGoogleGenerativeAI
import google.auth

_, PROJECT_ID = google.auth.default()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    temperature=0,
    project=PROJECT_ID,
    location="global",
    vertexai=True
)

agent = create_agent(
    llm,
    tools=[describe_file, query_file],
    system_prompt=SYSTEM_PROMPT
)


