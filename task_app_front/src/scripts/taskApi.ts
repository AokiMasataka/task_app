import { HOST, PORT } from "./const";

export type Task = {
    title: String;
    content: String;
    id: String
};

export type Tasks = Record<Task>;

export async function fetchTasksAPI(): Tasks {
    const response = await fetch(
        `http://${HOST}:${PORT}/task`,
        {
            method: "GET",
            headers: {"content-type": "application/json"}
        }
    );
    const tasks = (await response.json()).tasks;
    return tasks;
}

export async function fetchTaskAPI(id: String): Task {
    const response = await fetch(
        `http://${HOST}:${PORT}/task/${id}`,
        {
            method: "GET",
            headers: {"content-type": "application/json"}
        }
    );
    const task = (await response.json());
    return task;
}

export async function postTaskAPI(title: String, content: String) {
    const response = await fetch(
        `http://${HOST}:${PORT}/task`,
        {
            method: "POST",
            headers: {"content-type": "application/json"},
            body: JSON.stringify({title: title, content: content})
        }
    );

    const task_id = (await response.json()).task_id;
    return task_id;
}

export async function updateTaskAPI(
    id: String,
    title: String,
    content: String
) {
    const response = await fetch(
        `http://${HOST}:${PORT}/task/${id}`,
        {
            method: "PUT",
            headers: {"content-type": "application/json"},
            body: JSON.stringify({title: title, content: content})
        }
    );
    
}

export async function deleteTaskAPI(id: String) {
    const response = await fetch(
        `http://${HOST}:${PORT}/task/${id}`,
        {
            method: "DELETE",
            headers: {"content-type": "application/json"},
        }
    );
}