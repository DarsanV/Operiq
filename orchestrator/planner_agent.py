"""
planner_agent.py - The Planner AI
Breaks a big user task into smaller, manageable subtasks.
Uses Google Gemini (free tier).
"""

import google.generativeai as genai
import json
import os


class PlannerAgent:
    """
    The Planner AI reads the user's task and breaks it into
    a list of subtasks that other agents will execute.
    """

    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        # Use gemini-2.5-flash for stability and compatibility
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        print("✅ Planner Agent ready (Gemini 2.5 Flash).")

    def plan(self, task: str) -> list:
        """
        Given a task description, return a list of subtasks.

        Example:
            task = "Build a REST API for a todo app"
            returns = [
                "Create Todo model with id, title, done fields",
                "Create GET /todos endpoint",
                "Create POST /todos endpoint",
                "Create DELETE /todos/{id} endpoint"
            ]
        """
        prompt = f"""You are a software project planner.

A user wants to build: {task}

Break this into 3-5 clear, specific subtasks.
Return ONLY a JSON array of strings. No explanation. No markdown. No backticks.

Example output:
["Create the data model", "Build the API endpoints", "Add error handling"]
"""

        response = self.model.generate_content(prompt)
        try:
            raw = response.text.strip()
            # Clean up in case model adds backticks
            raw = raw.replace("```json", "").replace("```", "").strip()
        except Exception as e:
            print(f"Planner Agent Error accessing response text: {e}")
            raw = '["Analyze requirements", "Implement features", "Test implementation"]'

        try:
            plan = json.loads(raw)
            return plan
        except json.JSONDecodeError:
            # Fallback if parsing fails
            return [
                f"Analyze requirements for: {task}",
                "Implement core features",
                "Test the implementation"
            ]
