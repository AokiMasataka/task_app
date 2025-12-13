import { HOST, PORT, BACKEND_BASE_URL } from "./const.ts";
import { AllItems, Doc } from "./types.ts";

export async function fetchDocsAPI(projectId: string): Promise<AllItems<Doc>> {
    const response = await fetch(
        `${BACKEND_BASE_URL}projects/${projectId}/docs`,
        {
            method: "GET",
            headers: { "content-type": "application/json" },
        }
    );
    return await response.json();
}

export async function fetchDocAPI(
    projectId: string,
    docId: string
): Promise<Doc> {
    const response = await fetch(
        `${BACKEND_BASE_URL}projects/${projectId}/docs/${docId}`,
        {
            method: "GET",
            headers: { "content-type": "application/json" },
        }
    );
    return await response.json();
}

async function modifyDoc(doc: Doc, method: string, endpoint: string) {
    const requestUrl = new URL(endpoint, `${BACKEND_BASE_URL}`);
    const response = await fetch(requestUrl, {
        method: method,
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
            title: doc.title,
            content: doc.content,
        }),
    });
    return await response.json();
}

export async function postDocAPI(
    projectId: string,
    doc: Doc
): Promise<{ id: string }> {
    const endpoint = `projects/${projectId}/docs`;
    const response = await modifyDoc(doc, "POST", endpoint);
    return response;
}

export async function updateDocAPI(projectId: string, doc: Doc) {
    const endpoint = `projects/${projectId}/docs/${doc.id}`;
    await modifyDoc(doc, "PUT", endpoint);
}

export async function deleteDocAPI(projectId: string, id: string) {
    await fetch(`${BACKEND_BASE_URL}projects/${projectId}/docs/${id}`, {
        method: "DELETE",
        headers: { "content-type": "application/json" },
    });
}
