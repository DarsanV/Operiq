// App.js - Main application component
import React, { useState, useEffect } from 'react';
import TaskForm from './components/TaskForm';
import ResultPanel from './components/ResultPanel';
import TaskHistory from './components/TaskHistory';
import api from './services/api';
import './App.css';

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [currentResult, setCurrentResult] = useState(null);
  const [taskHistory, setTaskHistory] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadHistory();
  }, []);

  const loadHistory = async () => {
    try {
      const tasks = await api.getAllTasks();
      setTaskHistory(tasks);
    } catch (err) {
      console.log('Could not load history (backend might not be running)');
    }
  };

  const handleSubmitTask = async (task) => {
    setIsLoading(true);
    setError(null);
    setCurrentResult(null);

    try {
      const result = await api.submitTask(task);
      setCurrentResult(result);
      await loadHistory();
    } catch (err) {
      setError('ERR_CONNECTION_REFUSED: System unable to reach orchestration nodes. Ensure Spring Boot and Python agents are active.');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app">
      {/* Header */}
      <header className="app-header">
        <h1 className="operiq-brand">OPERIQ</h1>
        <p>Autonomous AI Orchestration Protocol</p>

        {/* Agent pipeline visualization */}
        <div className="pipeline">
          <span className="pipeline-step">SYS.PLANNER</span>
          <span className="arrow">/</span>
          <span className="pipeline-step">SYS.BACKEND</span>
          <span className="arrow">/</span>
          <span className="pipeline-step">SYS.DOCS</span>
          <span className="arrow">/</span>
          <span className="pipeline-step">DB.MONGO</span>
        </div>
      </header>

      {/* Main content */}
      <main className="app-main">
        {/* Task input form */}
        <TaskForm onSubmit={handleSubmitTask} isLoading={isLoading} />

        {/* Loading indicator */}
        {isLoading && (
          <div className="loading tech-panel">
            <div className="spinner"></div>
            <p>PROCESSING DIRECTIVE...</p>
            <p className="loading-sub">Allocating AI resources across orchestration protocol</p>
          </div>
        )}

        {/* Error message */}
        {error && <div className="error-message tech-panel">{error}</div>}

        {/* Result from agents */}
        {currentResult && <ResultPanel result={currentResult} />}

        {/* Task history from MongoDB */}
        <TaskHistory tasks={taskHistory} onSelect={setCurrentResult} />
      </main>
    </div>
  );
}

export default App;
