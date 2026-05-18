package com.multiagent.model;

import lombok.Data;
import java.util.List;

/**
 * TaskResponse - What we send back to the frontend after agents finish.
 */
@Data
public class TaskResponse {
    private String taskId;
    private String task;
    private List<String> plan;
    private String backendCode;
    private String documentation;
    private String status;
    private String createdAt;
}
