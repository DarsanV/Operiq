// services/api.js
// All API calls to the Spring Boot backend go here.

import axios from 'axios';

// The Spring Boot backend URL
const BASE_URL = 'http://localhost:8080/api';

const api = {
  /**
   * Submit a new task to the AI agents.
   * @param {string} task - The task description from the user
   * @returns {Promise} - The result with plan, code, and documentation
   */
  submitTask: async (task) => {
    const response = await axios.post(`${BASE_URL}/tasks`, { task });
    return response.data;
  },

  /**
   * Get all previously completed tasks.
   * @returns {Promise} - Array of completed tasks
   */
  getAllTasks: async () => {
    const response = await axios.get(`${BASE_URL}/tasks`);
    return response.data;
  },

  /**
   * Check if the backend is running.
   */
  healthCheck: async () => {
    const response = await axios.get(`${BASE_URL}/health`);
    return response.data;
  }
};

export default api;
