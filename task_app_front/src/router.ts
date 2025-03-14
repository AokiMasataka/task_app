import { createRouter, createWebHistory } from "vue-router";
import Doc from "./views/Doc.vue";
import Docs from "./views/Docs.vue";
import ProjectView from "./views/Project.vue";
import ProjectsView from "./views/Projects.vue";
import Tasks from "./views/Tasks.vue";

const routes = [
  { path: "/", redirect: "/projects" },
  { path: "/projects", name: "projects", component: ProjectsView },
  { path: "/projects/:projectId", name: "project", component: ProjectView },
  { path: "/projects/:projectId/docs/", name: "docs", component: Docs },
  { path: "/projects/:projectId/docs/:docId", name: "doc", component: Doc },
  { path: "/projects/:projectId/tasks", name: "tasks", component: Tasks },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
