package com.multiagent.service;

import com.multiagent.model.TaskRequest;
import com.multiagent.model.TaskResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.reactive.function.client.WebClientResponseException;

import java.util.List;
import java.util.Map;

/**
 * AgentService - The bridge between Spring Boot and the Python AI agents.
 * 
 * When the frontend sends a task, this service forwards it to the Python
 * orchestrator and returns the result back to the frontend.
 */
@Service
public class AgentService {

    private final WebClient webClient;

    // Python orchestrator URL (from application.properties)
    @Value("${orchestrator.url:http://localhost:5000}")
    private String orchestratorUrl;

    public AgentService(WebClient.Builder webClientBuilder) {
        this.webClient = webClientBuilder.build();
    }

    /**
     * Send a task to the Python orchestrator and get the AI-generated result.
     */
    public TaskResponse runTask(String task) {
        // Build request body
        Map<String, String> requestBody = Map.of("task", task);

        try {
            // Call the Python orchestrator
            Map response = webClient
                    .post()
                    .uri(orchestratorUrl + "/api/run-task")
                    .bodyValue(requestBody)
                    .retrieve()
                    .bodyToMono(Map.class)
                    .block(); // Wait for the response

            // Map the response to our TaskResponse object
            return mapToTaskResponse(response);
        } catch (WebClientResponseException e) {
            System.err.println("Orchestrator returned error: " + e.getResponseBodyAsString());
            TaskResponse errorResponse = new TaskResponse();
            errorResponse.setTaskId("ERROR");
            errorResponse.setTask(task);
            errorResponse.setStatus("failed");
            errorResponse.setDocumentation("AI Orchestrator Error: " + e.getResponseBodyAsString() + "\n\nThis usually means the AI API key ran out of its free rate-limit quota. Please wait a minute and try again.");
            return errorResponse;
        } catch (Exception e) {
            System.err.println("Failed to reach orchestrator: " + e.getMessage());
            TaskResponse errorResponse = new TaskResponse();
            errorResponse.setTaskId("ERROR");
            errorResponse.setTask(task);
            errorResponse.setStatus("failed");
            errorResponse.setDocumentation("System Error: Unable to reach the Python Orchestrator. Is it running?");
            return errorResponse;
        }
    }

    /**
     * Get all previously completed tasks from the orchestrator.
     */
    public List<TaskResponse> getAllTasks() {
        List<Map> responses = webClient
                .get()
                .uri(orchestratorUrl + "/api/tasks")
                .retrieve()
                .bodyToFlux(Map.class)
                .collectList()
                .block();

        return responses.stream()
                .map(this::mapToTaskResponse)
                .toList();
    }

    // Helper: convert raw Map to TaskResponse
    private TaskResponse mapToTaskResponse(Map data) {
        TaskResponse response = new TaskResponse();
        response.setTaskId((String) data.get("task_id"));
        response.setTask((String) data.get("task"));
        response.setPlan((List<String>) data.get("plan"));
        response.setBackendCode((String) data.get("backend_code"));
        response.setDocumentation((String) data.get("documentation"));
        response.setStatus((String) data.get("status"));
        response.setCreatedAt((String) data.get("created_at"));
        return response;
    }
}
