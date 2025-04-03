# tests/test_agent.py
import pytest
from agent.graph import build_travel_agent
from agent.state import AgentState

@pytest.fixture
def agent():
    return build_travel_agent()

def test_preference_extraction(agent):
    initial_state = AgentState(
        preferences={},
        destinations=[],
        itinerary={},
        history=[],
        user_input="I want a romantic trip to Europe for about a week with a budget of $2000.",
        is_followup=False
    )
    result = agent.invoke(initial_state)
    assert "romantic" in result["preferences"].lower()
    assert "europe" in result["preferences"].lower()

def test_destination_recommendation(agent):
    initial_state = AgentState(
        preferences={"input": "romantic trip to Europe"}, # Simplified for the test
        destinations=[],
        itinerary={},
        history=[],
        user_input="Okay, suggest some destinations.",
        is_followup=False
    )
    result = agent.invoke(initial_state)
    assert len(result["destinations"]) > 0

def test_complete_workflow(agent):
    initial_state = AgentState(
        preferences={},
        destinations=[],
        itinerary={},
        history=[],
        user_input="I want a cultural trip to Japan for 10 days.",
        is_followup=False
    )
    result = agent.invoke(initial_state)
    assert len(result["itinerary"]) > 0

def test_followup_question(agent):
    initial_state = AgentState(
        preferences={"input": "cultural trip to Japan"},
        destinations=[{"name": "Tokyo", "country": "Japan"}], #Minimal destination
        itinerary={"input": "Sample itinerary"},
        history=[],
        user_input="What are some good restaurants there?",
        is_followup=True
    )
    result = agent.invoke(initial_state)
    assert len(result["history"]) > 0