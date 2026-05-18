"""
orchestrator_agent.py - The Orchestrator
Coordinates all AI agents: Planner → Backend AI → Documentation AI → Save to DB
"""

import uuid
from datetime import datetime
from orchestrator.planner_agent import PlannerAgent
from orchestrator.backend_agent import BackendAgent
from orchestrator.documentation_agent import DocumentationAgent
from orchestrator.database import Database


class OrchestratorAgent:
    """
    The Orchestrator is the main coordinator.
    It receives a task, calls each agent in order, and combines the results.
    """

    def __init__(self):
        self.planner = PlannerAgent()
        self.backend_ai = BackendAgent()
        self.doc_ai = DocumentationAgent()
        self.db = Database()
        print("✅ Orchestrator initialized with all agents.")

    def run(self, task: str) -> dict:
        """
        Full pipeline:
        1. Planner AI breaks task into subtasks
        2. Backend AI generates code
        3. Documentation AI writes docs
        4. Results saved to MongoDB
        """
        task_id = str(uuid.uuid4())[:8]  # Short unique ID
        print(f"\n🚀 Starting task [{task_id}]: {task}")

        # Step 1: Plan the task
        print("🧠 Step 1: Planner AI is analyzing the task...")
        plan = self.planner.plan(task)
        print(f"📋 Plan: {plan}")

        # Step 2: Generate backend code
        print("💻 Step 2: Backend AI is writing code...")
        backend_code = self.backend_ai.generate(task, plan)

        # Step 3: Generate documentation
        print("📝 Step 3: Documentation AI is writing docs...")
        documentation = self.doc_ai.generate(task, backend_code)

        # Step 4: Combine everything
        result = {
            "task_id": task_id,
            "task": task,
            "plan": plan,
            "backend_code": backend_code,
            "documentation": documentation,
            "status": "completed",
            "created_at": datetime.utcnow().isoformat()
        }

        # Step 5: Save to MongoDB
        print("💾 Step 4: Saving results to MongoDB...")
        self.db.save_task(result)

        print(f"✅ Task [{task_id}] completed!")
        return result

    def get_all_tasks(self) -> list:
        """Fetch all completed tasks from the database."""
        return self.db.get_all_tasks()
