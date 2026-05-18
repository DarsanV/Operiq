# Architecture Guide

## How It All Works Together

```
[User types a task in React]
        ↓
[React calls Spring Boot: POST /api/tasks]
        ↓
[Spring Boot calls Python Orchestrator: POST /api/run-task]
        ↓
[Orchestrator calls Planner AI → gets a plan]
        ↓
[Orchestrator calls Backend AI → gets Java code]
        ↓
[Orchestrator calls Documentation AI → gets API docs]
        ↓
[All results saved to MongoDB]
        ↓
[Response travels back up to the React UI]
```

## File-by-File Explanation

### 🐍 Python Orchestrator (`/orchestrator`)

| File | What it does |
|------|-------------|
| `main.py` | Starts the Flask server |
| `routes.py` | Defines API endpoints (/api/run-task, /api/tasks) |
| `orchestrator_agent.py` | Coordinates all agents in the right order |
| `planner_agent.py` | Calls Claude API to break task into subtasks |
| `backend_agent.py` | Calls Claude API to generate Spring Boot code |
| `documentation_agent.py` | Calls Claude API to write API documentation |
| `database.py` | Connects to MongoDB and saves/reads tasks |

### ☕ Spring Boot Backend (`/backend`)

| File | What it does |
|------|-------------|
| `MultiAgentApplication.java` | Starts the Spring Boot server |
| `AgentController.java` | REST endpoints the React frontend calls |
| `AgentService.java` | Makes HTTP calls to the Python orchestrator |
| `TaskRequest.java` | Data class for incoming requests |
| `TaskResponse.java` | Data class for responses |

### ⚛️ React Frontend (`/frontend`)

| File | What it does |
|------|-------------|
| `App.js` | Main component, holds all state |
| `TaskForm.js` | Text input form for the user |
| `ResultPanel.js` | Shows plan, code, and docs in tabs |
| `TaskHistory.js` | Lists all past tasks from MongoDB |
| `services/api.js` | All API calls to Spring Boot |

## Data Flow Example

**User types**: "Build a REST API for a todo app"

1. **React** sends: `POST /api/tasks { "task": "Build a REST API for a todo app" }`
2. **Spring Boot** forwards to Python: `POST /api/run-task { "task": "..." }`
3. **Planner AI** returns: `["Create Todo model", "Build GET /todos", "Build POST /todos"]`
4. **Backend AI** returns: Full Java Spring Boot code
5. **Documentation AI** returns: Markdown API docs
6. **MongoDB** stores the complete result
7. **React** displays plan in tab 1, code in tab 2, docs in tab 3
