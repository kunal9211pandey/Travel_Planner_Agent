from typing import Dict, Any
from ..state import AgentState
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the user's question about the itinerary: {user_input}. Use this itinerary for context: {itinerary}"),
    ("user", "Okay, answer the question")
])

def handle_followup(state: AgentState) -> Dict[str, Any]:
    print("---HANDLING FOLLOW-UP---")
    user_input = state["user_input"]
    itinerary = state["itinerary"]
    messages = prompt.format_messages(user_input=user_input, itinerary=itinerary)
    response = model.invoke(messages)
    followup_answer = response.content
    print("Follow-up Answer:", followup_answer)
    return {"history": state["history"] + [{"user": user_input, "bot": followup_answer}]}