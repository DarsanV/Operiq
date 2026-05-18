# 🤖 Multi-Agent AI Platform

An autonomous multi-agent AI platform where specialized AI agents collaboratively analyze, divide, and execute software development tasks.

## 🏗️ Architecture

```
User → React Frontend → Spring Boot Backend → Orchestrator Agent
                                                      ↓
                                              Planner AI (breaks tasks)
                                            ↙              ↘
                                    Backend AI       Documentation AI
                                            ↘              ↙
                                         Final Combined Output
                                                  ↓
                                              MongoDB
                                                  ↓
                                          Final Response to User
```

## 📁 Project Structure

```
multi-agent-platform/
├── frontend/          → React UI (user talks to agents here)
├── backend/           → Spring Boot API (connects frontend to agents)
├── orchestrator/      → Python orchestrator + AI agents
└── docs/              → API documentation
```

## 🚀 Quick Start

### 1. Start the Orchestrator (Python AI Agents)
```bash
cd orchestrator
pip install -r requirements.txt
python main.py
```

### 2. Start the Backend (Spring Boot)
```bash
cd backend
./mvnw spring-boot:run
```

### 3. Start the Frontend (React)
```bash
cd frontend
npm install
npm start
```

### 4. Open the app
Visit `http://localhost:3000`

## 🔑 Environment Variables

Create `orchestrator/.env`:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get a free API key from: https://makersuite.google.com/app/apikey

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React |
| Backend | Spring Boot (Java) |
| AI Agents | Python + Google Gemini API |
| Database | Local JSON Storage |
| Agent Comm | REST APIs |
