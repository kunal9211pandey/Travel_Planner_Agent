from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from typing import Dict, List, Any
from .nodes.preference_extractor import extract_preferences
from .nodes.destination_finder import find_destinations
from .nodes.itinerary_creator import create_itinerary
from .nodes.followup_handler import handle_followup
from .state import AgentState
from .nodes.tools.weather_tool import get_weather  # Import the weather tool

def build_travel_agent():
    workflow = StateGraph(AgentState)

    #  Add nodes
    workflow.add_node("extract_preferences", extract_preferences)
    workflow.add_node("find_destinations", find_destinations)
    workflow.add_node("create_itinerary", create_itinerary)
    workflow.add_node("handle_followup", handle_followup)
    workflow.add_node("get_weather", get_weather)  # Add the weather tool node

    #  Add edges
    workflow.add_edge("extract_preferences", "find_destinations")
    workflow.add_edge("find_destinations", "create_itinerary")
    workflow.add_edge("create_itinerary", "get_weather")  # Add edge to weather tool

    workflow.add_conditional_edges(
        "create_itinerary",
        lambda state: "handle_followup" if state.get("is_followup") else "get_weather", # Modified conditional edge
    )

    workflow.add_edge("get_weather", "END")  # Edge from weather tool to END
    workflow.add_edge("handle_followup", "END")

    workflow.set_entry_point("extract_preferences")
    return workflow.compile()