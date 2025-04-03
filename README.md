# Travel Planner AI Agent

This project implements a Travel Planner AI agent using the LangGraph library. The agent assists users in planning trips by understanding their preferences, suggesting destinations, creating itineraries, and answering follow-up questions. [cite: 1, 2]

## Overview

The Travel Planner AI Agent leverages LangGraph to create a multi-step reasoning workflow for trip planning. It interacts with the user to gather preferences, suggests destinations based on those preferences, generates detailed itineraries, and provides helpful responses to user queries. [cite: 2, 3]

## Core Features

* **Understand User Preferences:** Extracts key travel preferences from user input, including budget, duration, and interests. [cite: 3]
* **Suggest Destinations:** Recommends appropriate travel destinations based on the user's stated preferences. [cite: 3]
* **Create Itineraries:** Generates detailed, day-by-day travel plans. [cite: 3]
* **Answer Follow-up Questions:** Provides responses to user questions and requests for modifications to the suggested travel plans. [cite: 3]

## Technologies Used

* **LangGraph:** Used to construct the multi-step reasoning workflow. [cite: 3, 1]
* **LangChain:** Facilitates integration with LLMs. [cite: 11]
* **OpenAI API:** Provides access to the LLM. [cite: 11]
* **Python:** The primary programming language. [cite: 4]
* **Flask:** Used to create a basic web application. [cite: 4]
* **JSON:** Used for the mock destination database. [cite: 4, 8, 9]

## Approach

The project is structured as follows:

* **LangGraph Workflow:** A directed graph is implemented using LangGraph, where each node represents a step in the travel planning process. [cite: 7]
* **State Management:** User preferences and planning progress are tracked using a state object. [cite: 7]
* **External Tools:** The agent interacts with a mock destination database and a mock weather API to provide relevant information. [cite: 3]

The main steps in the workflow are:

1.  **Preference Extraction:** The `PreferenceExtractor` node extracts travel preferences from the user's input. [cite: 7]
2.  **Destination Finding:** The `DestinationFinder` node suggests destinations based on the extracted preferences. [cite: 7]
3.  **Itinerary Creation:** The `ItineraryCreator` node generates a detailed itinerary. [cite: 7]
4.  **Follow-up Handling:** The `FollowUpHandler` node addresses any follow-up questions from the user. [cite: 7]

## Project Structure

travel_planner/
main.py         # Entry point for the application
agent/
graph.py      # LangGraph implementation
nodes/
tools/   # External tool connections
state.py      # State management
data/
destinations.json  # Mock destination database
tests/
test_agent.py   # Test cases
README.md       # Documentation


## Setup Instructions

1.  **Prerequisites:**

    * Python 3.7+
    * Git
    * VS Code (Recommended)

2.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd travel_planner
    ```

3.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate # For macOS/Linux
    venv\Scripts\activate # For Windows
    ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up OpenAI API Key:**

    * Create a `.env` file in the root directory.
    * Add your OpenAI API key to the `.env` file:

        ```
        OPENAI_API_KEY=YOUR_API_KEY
        ```

    * **Note:** Do not commit the `.env` file. Add it to `.gitignore`.

## Running the Application

1.  To run the application, execute the following command in the terminal:

    ```bash
    python main.py
    ```

2.  The application will start, and you can interact with the Travel Planner AI agent.

## Additional Notes

* The project includes basic error handling.
* The project uses a mock destination database and a mock weather API.
* Further development can include integrating with real APIs and improving the user interface.
