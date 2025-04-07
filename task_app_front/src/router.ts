import { createRouter, createWebHistory } from "vue-router";
// import Doc from "./views/Doc.vue";
// import Docs from "./views/Docs.vue";
// import NewDoc from "./views/NewDoc.vue";
// import UpdateDoc from "./views/UpdateDoc.vue";
import Docs from "./views/Docs";
// import Doc from "./views/Doc";
import Doc from "./views/Project/Docs/Docs.vue";
import DocNew from "./views/DocNew";
import DocUpdate from "./views/DocUpdate";
import Project from "./views/Project";
import Projects from "./views/Projects";

import Tasks from "./views/Tasks.vue";

const routes = [
    { path: "/", redirect: "/projects" },
    { path: "/projects", name: "projects", component: Projects },
    { path: "/projects/:projectId", name: "project", component: Project },
    { path: "/projects/:projectId/tasks", name: "tasks", component: Tasks },
    { path: "/projects/:projectId/docs/", name: "docs", component: Docs },
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
