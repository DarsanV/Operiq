package com.multiagent.model;

import lombok.Data;
import java.util.List;

/**
 * TaskRequest - What the frontend sends to us.
 * Example: { "task": "Build a REST API for a todo app" }
 */
@Data
public class TaskRequest {
    private String task;
}
