// components/TaskForm.js
import React, { useState } from 'react';

function TaskForm({ onSubmit, isLoading }) {
  const [task, setTask] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (task.trim()) {
      onSubmit(task);
      setTask('');
    }
  };

  const exampleTasks = [
    'INIT: REST API / todo_app / auth_module',
    'INIT: microservice / inventory_mgmt / spring_boot',
    'INIT: websocket_gateway / messaging_system',
    'INIT: payment_processor / secure_transaction_layer',
  ];

  return (
    <div className="task-form-container tech-panel">
      <h2>INITIALIZE DIRECTIVE</h2>
      <p className="subtitle">Enter specifications. Operiq agents will construct the required architecture.</p>

      <form onSubmit={handleSubmit}>
        <textarea
          value={task}
          onChange={(e) => setTask(e.target.value)}
          placeholder="> Input architectural requirements here..."
          disabled={isLoading}
        />
        <button type="submit" disabled={isLoading || !task.trim()}>
          {isLoading ? 'EXECUTING...' : 'DEPLOY PROTOCOL'}
        </button>
      </form>

      <div className="examples">
        <p>SUGGESTED MACROS:</p>
        <div className="example-badges">
          {exampleTasks.map((example, i) => (
            <button
              key={i}
              className="example-btn"
              onClick={() => setTask(example)}
              disabled={isLoading}
            >
              {example}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}

export default TaskForm;
