import { createRouter, createWebHistory } from "vue-router";
import Doc from "./views/Doc.vue";
import Docs from "./views/Docs.vue";
import NewDoc from "./views/NewDoc.vue";
import ProjectView from "./views/Project.vue";
import ProjectsView from "./views/Projects.vue";
import Tasks from "./views/Tasks.vue";
import UpdateDoc from "./views/UpdateDoc.vue";

const routes = [
    { path: "/", redirect: "/projects" },
    { path: "/projects", name: "projects", component: ProjectsView },
    { path: "/projects/:projectId", name: "project", component: ProjectView },
    { path: "/projects/:projectId/tasks", name: "tasks", component: Tasks },
    { path: "/projects/:projectId/docs/", name: "docs", component: Docs },
    {
        path: "/projects/:projectId/docs/new",
        name: "new docs",
        component: NewDoc,
    },
    { path: "/projects/:projectId/docs/:docId", name: "doc", component: Doc },
    {
        path: "/projects/:projectId/docs/:docId/edit",
        name: "edit docs",
        component: UpdateDoc,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
