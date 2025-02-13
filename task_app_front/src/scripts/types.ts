export type TaskForShow = Omit<Task, "status"> & {status: {state: string, value: number}}

export type Task = {
    title: string;
    content: string;
    id: string;
    status: number;
    priority: number;
    duedate: Date | null;
};

export type Tasks = Task[];

export const CreateInitTaskData = (status: number): Task => {
    return {
        title: "",
        content: "",
        id: "",
        status: status,
        priority: 0,
        duedate: null
    };
};