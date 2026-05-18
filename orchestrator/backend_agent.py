"""
backend_agent.py - The Backend AI
Generates backend code (Java Spring Boot) based on the task and plan.
Uses Google Gemini (free tier).
"""

import google.generativeai as genai
import os


class BackendAgent:
    """
    The Backend AI takes the task and plan, then generates
    production-ready Spring Boot backend code.
    """

    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        print("✅ Backend Agent ready (Gemini 2.5 Flash).")

    def generate(self, task: str, plan: list) -> str:
        """
        Given a task and its subtasks, generate Spring Boot code.

        Returns:
            A string containing the generated Java code.
        """
        plan_text = "\n".join([f"- {step}" for step in plan])

        prompt = f"""You are an expert Spring Boot developer.

Generate clean, beginner-friendly Spring Boot (Java) code for this task:
Task: {task}

The plan is:
{plan_text}

Requirements:
- Use Spring Boot with REST controllers
- Include a model class, service class, and controller class
- Add helpful comments explaining each part
- Keep it simple and readable for beginners

Return only the code. No explanation outside the code comments.
"""

        response = self.model.generate_content(prompt)
        try:
            return response.text.strip()
        except Exception as e:
            return f"// Code generation failed due to safety settings or empty response.\n// Error: {e}"
