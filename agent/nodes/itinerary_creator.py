from typing import Dict, Any
from ..state import AgentState
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Create a detailed itinerary based on these destinations: {destinations}. Include daily activities, estimated costs, and weather information: {weather}."),
    ("user", "Okay, create an itinerary")
])

def create_itinerary(state: AgentState) -> Dict[str, Any]:
    print("---CREATING ITINERARY---")
    destinations = state["destinations"]
    weather = state["weather"]
    messages = prompt.format_messages(destinations=destinations, weather=weather)
    response = model.invoke(messages)
    itinerary = response.content
    print("Created Itinerary:", itinerary)
    return {"itinerary": itinerary}