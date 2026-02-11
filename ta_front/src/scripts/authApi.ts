import { BACKEND_BASE_URL } from '@/scripts/const';


export async function createAccount(
    name: string,
    email: string,
    pass: string
): Promise<{ id: string }> {
    const url = new URL("/api/users", BACKEND_BASE_URL).toString();

    const headers = new Headers();
    headers.append("Content-Type", "application/json");
    const response = await fetch(
        url,
        {
            method: "POST",
            headers: headers,
            body: JSON.stringify({ name: name, email: email, password: pass }),
        }
    );
    return await response.json();
}


export async function get_user(user_id: string) {
    const url = new URL(`/api/users/${user_id}`, BACKEND_BASE_URL).toString();
    const headers = new Headers();
    headers.append("Content-Type", "application/json");
    const response = await fetch(
        url,
        {
            method: "GET",
            headers: headers,
        }
    );
    return await response.json();
}


export async function get_users() {
    const url = new URL(`/api/users`, BACKEND_BASE_URL).toString();
    const headers = new Headers();
    headers.append("Content-Type", "application/json");
    const response = await fetch(
        url,
        {
            method: "GET",
            headers: headers,
        }
    );
    return await response.json();
}

export async function me(token: string) {
    const payload = parseJwt(token)
    const m = await get_user(payload.id);
    return m;
}


function parseJwt(token: string) {
  const base64Url = token.split('.')[1];
  const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
  const json = decodeURIComponent(
    atob(base64)
      .split('')
      .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
      .join('')
  );

  return JSON.parse(json);
}
