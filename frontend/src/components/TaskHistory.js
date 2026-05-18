// components/TaskHistory.js
import React from 'react';

function TaskHistory({ tasks, onSelect }) {
  if (!tasks || tasks.length === 0) {
    return (
      <div className="tech-panel task-history">
        <h3>OPERATION LOG</h3>
        <div className="history-empty">
          <p>NO PREVIOUS PROTOCOLS EXECUTED.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="tech-panel task-history">
      <h3>OPERATION LOG</h3>
      <div className="history-list">
        {tasks.map((task) => (
          <div
            key={task.taskId || task.id}
            className="history-item"
            onClick={() => onSelect(task)}
          >
            <span className="history-id">ID:{task.taskId || task.id || 'NULL'}</span>
            <span className="history-task">{task.task}</span>
            <span className="history-status">STATUS:{task.status || 'OK'}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default TaskHistory;
