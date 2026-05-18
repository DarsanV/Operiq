"""
database.py - Local JSON Storage Connection
Saves and retrieves completed tasks from a local JSON file.
"""

import json
import os


class Database:
    """
    Simple Local JSON wrapper.
    Saves completed task results and retrieves them later without needing
    MongoDB.
    """

    def __init__(self):
        self.db_file = "database.json"
        print("✅ Connected to Local JSON Database.")
        if not os.path.exists(self.db_file):
            with open(self.db_file, "w") as f:
                json.dump([], f)

    def save_task(self, task_data: dict):
        """Save a completed task result to JSON file."""
        # Remove _id if it exists to avoid conflicts
        task_data.pop("_id", None)

        tasks = self.get_all_tasks()
        tasks.insert(0, task_data)  # insert at beginning (newest first)

        with open(self.db_file, "w") as f:
            json.dump(tasks, f, indent=4)

        print(f"💾 Task {task_data.get('task_id')} saved to local database.")

    def get_all_tasks(self) -> list:
        """Retrieve all tasks, newest first."""
        if not os.path.exists(self.db_file):
            return []
        try:
            with open(self.db_file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
