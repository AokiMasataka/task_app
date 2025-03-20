// export type TaskForShow = Omit<Task, "status"> & {
//     status: { state: string; value: number };
// };

export type TaskID = string;
export type ProjectID = string;

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

export type Project = {
    id: string;
    title: string;
    description: string;
};

export type Projects = Project[];
