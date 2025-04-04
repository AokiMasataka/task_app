import { createRouter, createWebHistory } from "vue-router";
import Doc from "./views/Doc/index.ts";
import DocNew from "./views/DocNew/index.ts";
import DocUpdate from "./views/DocUpdate/index.ts";
import Project from "./views/Project/index.ts";
import Projects from "./views/Projects/index.ts";

const routes = [
    { path: "/", redirect: "/projects" },
    { path: "/projects", name: "projects", component: Projects },
    {
        path: "/projects/:projectId/:tabName",
        name: "project",
        component: Project,
    },
    {
        path: "/projects/:projectId",
        redirect: (to: any) => {
            if (to.path.endsWith("/")) return to.path + "tasks";

            return to.path + "/tasks";
        },
    },
    {
        path: "/projects/:projectId/docs/new",
        name: "new docs",
        component: DocNew,
    },
    { path: "/projects/:projectId/docs/:docId", name: "doc", component: Doc },
    {
        path: "/projects/:projectId/docs/:docId/edit",
        name: "edit docs",
        component: DocUpdate,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
