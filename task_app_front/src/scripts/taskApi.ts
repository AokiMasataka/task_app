import { HOST, PORT } from "./const.ts";
import { Task, Tasks } from "./types.ts";


export async function fetchTasksAPI(status: number): Promise<Tasks> {
    const response = await fetch(
        `http://${HOST}:${PORT}/task?status=${status}`,
        {
            method: "GET",
            headers: {"content-type": "application/json"},
        }
    );
    const tasks = (await response.json()).tasks;
    return tasks;
}

export async function fetchTaskAPI(id: string): Promise<Task> {
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

export async function postTaskAPI(title: string, content: string, status: number): Promise<string> {
    const response = await fetch(
        `http://${HOST}:${PORT}/task`,
        {
            method: "POST",
            headers: {"content-type": "application/json"},
            body: JSON.stringify({title: title, content: content, status: status})
        }
    );

    const task_id = (await response.json()).task_id;
    return task_id;
}

export async function updateTaskAPI(
    id: string,
    title: string,
    content: string,
    status: number,
) {
    await fetch(
        `http://${HOST}:${PORT}/task/${id}`,
        {
            method: "PUT",
            headers: {"content-type": "application/json"},
            body: JSON.stringify({title: title, content: content, status: status})
        }
    );
    
}

export async function deleteTaskAPI(id: string) {
    await fetch(
        `http://${HOST}:${PORT}/task/${id}`,
        {
            method: "DELETE",
            headers: {"content-type": "application/json"},
        }
    );
}