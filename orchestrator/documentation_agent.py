"""
documentation_agent.py - The Documentation AI
Reads the generated code and writes clear API documentation.
Uses Google Gemini (free tier).
"""

import google.generativeai as genai
import os


class DocumentationAgent:
    """
    The Documentation AI reads the backend code and automatically
    generates API documentation in Markdown format.
    """

    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        print("✅ Documentation Agent ready (Gemini 2.5 Flash).")

    def generate(self, task: str, code: str) -> str:
        """
        Given the task and generated code, write API documentation.

        Returns:
            A Markdown string with the full API docs.
        """
        prompt = f"""You are a technical writer.

Read this Spring Boot code and write clear API documentation
in Markdown format.

Original Task: {task}

Generated Code:
{code}

Write documentation that includes:
1. Overview of what was built
2. API Endpoints (method, URL, request body, response)
3. Example requests using curl
4. How to run the application

Keep it beginner-friendly and easy to follow.
"""

        response = self.model.generate_content(prompt)
        try:
            return response.text.strip()
        except Exception as e:
            return f"# Documentation Error\n\nDocumentation could not be generated due to API issues.\n\nError: {e}"
