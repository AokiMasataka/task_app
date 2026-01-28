import { BACKEND_BASE_URL } from "./const.ts";


export async function login(
    name: string,
    pass: string
): Promise<{ token: string }> {
    const response = await fetch(`${BACKEND_BASE_URL}/login`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ name, pass }),
    });
    return await response.json();
}

export async function register(
    name: string,
    email: string,
    pass: string
): Promise<{ token: string }> {
    const response = await fetch(`${BACKEND_BASE_URL}/register`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ name, email, pass }),
    });
    return await response.json();
}