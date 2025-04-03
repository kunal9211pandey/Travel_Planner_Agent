from typing import Dict, List, Any, TypedDict

class AgentState(TypedDict):
    preferences: Dict[str, Any]
    destinations: List[Dict[str, Any]]
    itinerary: Dict[str, Any]
    history: List[Dict[str, str]]
    user_input: str
    is_followup: bool
    weather: Dict[str, str]  # Add weather to the state