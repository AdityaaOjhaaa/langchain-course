from dotenv import load_dotenv
import os
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

load_dotenv()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet.
    Args:
        query: The query to search for.
    Returns:
        The search result.
    """
    print(f"Searching the web for {query}")
    return "Tokyo weather is sunny with a temperature of 22°C"

# Initialize the LLM with correct model name
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",  # Changed to available model
    google_api_key=os.environ.get("GEMINI_API_KEY")
)

# Define tools
tools = [search]

# Create the agent
agent_executor = create_react_agent(llm, tools)

def main():
    print("Hello from langchain-course!")
    result = agent_executor.invoke({"messages": [("user", "What is the weather in Tokyo?")]})
    print("\nFinal Answer:")
    print(result["messages"][-1].content)

if __name__ == "__main__":
    main()
