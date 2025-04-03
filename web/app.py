# web/app.py
from flask import Flask, render_template, request, jsonify
from agent.graph import build_travel_agent
from agent.state import AgentState

app = Flask(__name__)
agent = build_travel_agent()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        initial_state = AgentState(
            preferences={},
            destinations=[],
            itinerary={},
            history=[],
            user_input=user_input,
            is_followup=False
        )
        result = agent.invoke(initial_state | {"user_input": user_input})
        return jsonify(result)  # Return result as JSON
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)