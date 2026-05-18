"""
routes.py - Flask API routes
Exposes endpoints that the Spring Boot backend calls.
"""

from flask import request, jsonify
from orchestrator.orchestrator_agent import OrchestratorAgent

# One orchestrator instance handles all requests
orchestrator = OrchestratorAgent()


def register_routes(app):

    @app.route("/health", methods=["GET"])
    def health():
        """Simple health check endpoint."""
        res_data = {
            "status": "ok",
            "message": "Multi-Agent Platform is running!"
        }
        return jsonify(res_data)

    @app.route("/api/run-task", methods=["POST"])
    def run_task():
        """
        Main endpoint: receives a user task, runs all agents,
        and returns combined output.

        Request body:
            { "task": "Build a REST API for a todo app" }

        Response:
            {
                "task_id": "...",
                "plan": [...],
                "backend_code": "...",
                "documentation": "...",
                "status": "completed"
            }
        """
        data = request.get_json()

        if not data or "task" not in data:
            return jsonify({"error": "Please provide a 'task' field."}), 400

        task = data["task"]
        print(f"\n[INFO] New Task Received: {task}")

        try:
            result = orchestrator.run(task)
            return jsonify(result), 200
        except Exception as e:
            print(f"[ERROR] {e}")
            return jsonify({"error": str(e)}), 500

    @app.route("/api/tasks", methods=["GET"])
    def get_tasks():
        """Returns all previously completed tasks from MongoDB."""
        tasks = orchestrator.get_all_tasks()
        return jsonify(tasks), 200
