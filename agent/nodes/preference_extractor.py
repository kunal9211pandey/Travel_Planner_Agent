from typing import Dict, Any
from ..state import AgentState
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv


load_dotenv()  # Load environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=openai_api_key) # Or any other suitable model

prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract user preferences for a trip. Identify budget, duration, interests, and any specific destinations."),
    ("user", "{user_input}")
])

def extract_preferences(state: AgentState) -> Dict[str, Any]:
    print("---EXTRACTING PREFERENCES---")
    messages = prompt.format_messages(user_input=state["user_input"])
    response = model.invoke(messages)
    preferences = response.content
    print("Extracted Preferences:", preferences)
    return {"preferences": preferences}