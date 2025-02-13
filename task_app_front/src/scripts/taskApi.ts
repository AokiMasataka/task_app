import { HOST, PORT } from "./const.ts";
import { dateToString, stringToDate } from "./date.ts";
import { Task, Tasks } from "./types.ts";

export async function fetchTasksAPI(status: number): Promise<Tasks> {
    const response = await fetch(
        `http://${HOST}:${PORT}/task?status=${status}`,
        {
            method: "GET",
            headers: {"content-type": "application/json"},
        }
    );
    const rawTasks: (Omit<Task, "duedate"> & {duedate: string|null})[] = (await response.json()).tasks;
    const tasks = rawTasks.map(t => {
        return {
            ...t,
            duedate:t.duedate == null ? null : stringToDate(t.duedate) 
        }
    });
    
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
    if (task.duedate !== null) {
       task.duedate = stringToDate(task.duedate);
    }
    return task;
}

async function modifyTask(task: Task, method: "POST"|"PUT") {
    const path = method === "POST" ? "/task" : `/task/${task.id}`
    const requestUrl = new URL(path, `http://${HOST}:${PORT}`)
    await fetch(
        requestUrl,{
            method: method,
            headers: {"content-type": "application/json"},
            body: JSON.stringify({
                title: task.title,
                content: task.content,
                status: task.status,
                priority: task.priority,
                duedate: task.duedate == null ? null : dateToString(task.duedate)
            })
        }
    );
}

export async function postTaskAPI(task: Task) {
    await modifyTask(task, "POST");
}

export async function updateTaskAPI(task: Task) {
    await modifyTask(task, "PUT");
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