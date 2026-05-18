package com.multiagent;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Main entry point for the Spring Boot backend.
 * This connects the React frontend to the Python orchestrator.
 */
@SpringBootApplication
public class MultiAgentApplication {
    public static void main(String[] args) {
        SpringApplication.run(MultiAgentApplication.class, args);
        System.out.println("✅ Spring Boot backend running on http://localhost:8080");
    }
}
