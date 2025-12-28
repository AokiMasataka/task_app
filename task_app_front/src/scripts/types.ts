// export type TaskForShow = Omit<Task, "status"> & {
//     status: { state: string; value: number };
// };

export type ProjectID = string;
export type TaskID = string;
export type DocID = string;


// Project types
export type Project = {
    id: string;
    name: string;
    description: string;
};

export type Projects = Project[];


// Task types
export type Task = {
    id: string;
    project_id: string;
    title: string;
    content: string;
    status: number;
    priority: number;
    duedate: Date | null;
};

export type Tasks = Task[];

export const CreateInitTaskData = (status: number): Task => {
    return {
        id: "",
        project_id: "",
        title: "",
        content: "",
        status: status,
        priority: 0,
        duedate: null,
    };
};


// Doc types
export type Doc = {
    id: string;
    project_id: string;
    title: string;
    content: string;
};

export type Docs = Doc[];


export type AllItems<T> = {
    count: number;
    prev: string | null;
    next: string | null;
    results: T[]
}