import { BACKEND_BASE_URL } from "./const.ts";
import { dateToString, stringToDate } from "./date.ts";
import { Task, Tasks } from "./types.ts";

export async function fetchTasksAPI(
    projectId: string,
    status: number
): Promise<Tasks> {
    const response = await fetch(
        `${BACKEND_BASE_URL}/projects/${projectId}/tasks?status=${status}`,
        {
            method: "GET",
            headers: { "content-type": "application/json" },
        }
    );
    const rawTasks: (Omit<Task, "duedate"> & { duedate: string | null })[] = (
        await response.json()
    ).results;
    const tasks = rawTasks.map((t) => {
        return {
            ...t,
            duedate: t.duedate == null ? null : stringToDate(t.duedate),
        };
    });

    return tasks;
}

export async function fetchTaskAPI(
    projectId: string,
    id: string
): Promise<Task> {
    const response = await fetch(
        `${BACKEND_BASE_URL}/projects/${projectId}/tasks/${id}`,
        {
            method: "GET",
            headers: { "content-type": "application/json" },
        }
    );
    const task = await response.json();
    if (task.duedate !== null) {
        task.duedate = stringToDate(task.duedate);
    }
    return task;
}

async function modifyTask(
    projectId: string,
    task: Task,
    method: "POST" | "PUT"
) {
    let url = "";
    if (method === "PUT") {
        url = `${BACKEND_BASE_URL}/projects/${projectId}/tasks/${task.id}`;
    } else {
        url = `${BACKEND_BASE_URL}/projects/${projectId}/tasks`;
    };
    await fetch(url, {
        method: method,
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
            title: task.title,
            content: task.content,
            status: task.status,
            priority: task.priority,
            duedate: task.duedate == null ? null : dateToString(task.duedate),
        }),
    });
}

export async function postTaskAPI(projectId: string, task: Task) {
    await modifyTask(projectId, task, "POST");
}

export async function updateTaskAPI(projectId: string, task: Task) {
    await modifyTask(projectId, task, "PUT");
}

export async function deleteTaskAPI(projectId: string, id: string) {
    await fetch(`${BACKEND_BASE_URL}/projects/${projectId}/tasks/${id}`, {
        method: "DELETE",
        headers: { "content-type": "application/json" },
    });
}
