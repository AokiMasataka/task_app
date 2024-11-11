export type TaskForShow = Omit<Task, "status"> & {status: {state: string, value: number}}

export type Task = {
    title: string;
    content: string;
    id: string;
    status: number;
};

export type Tasks = Task[];