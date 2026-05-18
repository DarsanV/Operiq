package com.multiagent.controller;

import com.multiagent.model.TaskRequest;
import com.multiagent.model.TaskResponse;
import com.multiagent.service.AgentService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * AgentController - The REST API that the React frontend calls.
 *
 * Endpoints:
 *   POST /api/tasks      → Submit a new task to the AI agents
 *   GET  /api/tasks      → Get all completed tasks
 *   GET  /api/health     → Check if the backend is running
 */
@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:3000")  // Allow React frontend
public class AgentController {

    private final AgentService agentService;

    public AgentController(AgentService agentService) {
        this.agentService = agentService;
    }

    /**
     * Health check - tells you if the backend is running.
     * GET http://localhost:8080/api/health
     */
    @GetMapping("/health")
    public ResponseEntity<String> health() {
        return ResponseEntity.ok("✅ Backend is running!");
    }

    /**
     * Submit a task to the AI agents.
     * POST http://localhost:8080/api/tasks
     * Body: { "task": "Build a REST API for a todo app" }
     */
    @PostMapping("/tasks")
    public ResponseEntity<TaskResponse> runTask(@RequestBody TaskRequest request) {
        System.out.println("📥 Received task: " + request.getTask());
        TaskResponse result = agentService.runTask(request.getTask());
        return ResponseEntity.ok(result);
    }

    /**
     * Get all previously completed tasks.
     * GET http://localhost:8080/api/tasks
     */
    @GetMapping("/tasks")
    public ResponseEntity<List<TaskResponse>> getAllTasks() {
        List<TaskResponse> tasks = agentService.getAllTasks();
        return ResponseEntity.ok(tasks);
    }
}
