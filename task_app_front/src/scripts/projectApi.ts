import { BACKEND_BASE_URL } from "./const.ts";
import { Project, Projects } from "./types.ts";

export async function fetchProjectsAPI(): Promise<Projects> {
    const response = await fetch(`${BACKEND_BASE_URL}/projects`, {
        method: "GET",
        headers: { "content-type": "application/json" },
    });
    const projects: Projects = (await response.json()).results;
    return projects;
}

export async function fetchProjectAPI(id: string): Promise<Project> {
    const response = await fetch(`${BACKEND_BASE_URL}/projects/${id}`, {
        method: "GET",
        headers: { "content-type": "application/json" },
    });
    const project = await response.json();
    return project;
}

async function modifyProject(project: Project, method: "POST" | "PUT") {
    let url = "";
    if (method === "PUT") {
        url = `${BACKEND_BASE_URL}/projects/${project.id}`;
    } else {
        url = `${BACKEND_BASE_URL}/projects`;
    };
    
    await fetch(url, {
        method: method,
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
            name: project.name,
            description: project.description,
        }),
    });
}

export async function createProjectAPI(project: Project) {
    await modifyProject(project, "POST");
}

export async function updateProjectAPI(project: Project) {
    await modifyProject(project, "PUT");
}

export async function deleteProjectAPI(id: string) {
    await fetch(`${BACKEND_BASE_URL}/projects/${id}`, {
        method: "DELETE",
        headers: { "content-type": "application/json" },
    });
}
