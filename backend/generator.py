from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from .config import GEMINI_API_KEY

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    google_api_key=GEMINI_API_KEY,
    temperature=0.7,
)


def generate_content(prompt: str) -> str:
    """Send prompt to Gemini model and return the generated text."""
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
