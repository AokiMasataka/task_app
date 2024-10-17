export const HOST = "localhost";
export const PORT = "8000";


export const state = {
    Todo: 0,
    Doing: 1,
    Done: 2
};

export const items = Object.entries(state).map(([text, value]) => {
    return {
        text,
        value
    }
});