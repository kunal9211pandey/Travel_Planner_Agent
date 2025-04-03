import json
from typing import Dict, List, Any
from ..state import AgentState
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Load the destination database
with open("data/destinations.json", "r") as f:
    destinations_data = json.load(f)

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Find destinations based on user preferences: {preferences}.  Return a list of destination names."),
    ("user", "Okay, find some destinations")
])


def find_destinations(state: AgentState) -> Dict[str, Any]:
    print("---FINDING DESTINATIONS---")
    preferences = state["preferences"]
    messages = prompt.format_messages(preferences=preferences)
    response = model.invoke(messages)
    destination_names = response.content
    print("LLM suggested destinations:", destination_names)

    #  Filter destinations from the database (replace with more sophisticated logic)
    #  This is a placeholder - you'll need to implement actual filtering
    found_destinations = [
        dest for dest in destinations_data
        if dest["name"] in destination_names #Very basic filtering
    ]

    print("Found Destinations:", found_destinations)
    return {"destinations": found_destinations}