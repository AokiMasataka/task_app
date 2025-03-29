<template>
    <div class="mx-8 my-4">
        <v-btn class="my-4" @click="openCreateForm">New Project</v-btn>

        <v-data-table-server
            :items="projects"
            :headers="headers"
            :items-per-page="projects.length"
            :loading="loading"
            :items-length="projects.length"
            :hover="true"
            no-data-text="does not projects"
            @click:row="handleClick"
        >
            <template v-slot:item.actions="{ item }">
                <div class="d-flex ga-2 justify-end">
                    <v-icon :icon="Pencil" @click.stop="openUpdateForm(item)" />
                    <v-icon :icon="Trash" @click.stop="openDeleteForm(item)" />
                </div>
            </template>
        </v-data-table-server>

        <v-dialog v-model="dialog" width="800">
            <ProjectForm
                :title="formProps.formTitle"
                v-model="formProps.project"
                @on-close="closeForm"
                @on-save="formProps.onSave"
            />
        </v-dialog>

        <v-dialog v-model="deleteDialog" width="800">
            <DeleteForm
                title="Delete Project?"
                @on-close="closeDeleteForm"
                @on-delete="deleteProject"
            />
        </v-dialog>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import DeleteForm from "../components/DeleteForm";
import Pencil from "../components/icons/Pencil.vue";
import Trash from "../components/icons/Trash.vue";
import ProjectForm from "../components/ProjectForm";
import {
    createProjectAPI,
    deleteProjectAPI,
    fetchProjectsAPI,
    updateProjectAPI,
} from "../scripts/projectApi";
import { Project, Projects } from "../scripts/types";

const loading = ref(false);
const router = useRouter();
const projects = ref<Projects>([]);

const dialog = ref<boolean>(false);
const deleteDialog = ref<boolean>(false);

const formProps = ref<{
    formTitle: string;
    project: Project;
    onSave: () => {};
}>({
    formTitle: "",
    project: { id: "", title: "", description: "" },
    onSave: async () => {},
});

const headers = [
    { title: "title", value: "title", align: "end" },
    { title: "description", value: "description", align: "end" },
    { title: "Actions", value: "actions", align: "end", sortable: false },
];

async function fetchProjects() {
    loading.value = true;
    try {
        projects.value = await fetchProjectsAPI();
    } finally {
        loading.value = false;
    }
}

function openCreateForm() {
    formProps.value.formTitle = "Create New Project";
    formProps.value.project = { id: "", title: "", description: "" };
    formProps.value.onSave = cretaeProject;
    dialog.value = true;
}

function openUpdateForm(project: Project) {
    formProps.value.formTitle = "Update Project";
    formProps.value.project = { ...project };
    formProps.value.onSave = updateProject;
    dialog.value = true;
}

function closeForm() {
    dialog.value = false;
}

async function cretaeProject() {
    await createProjectAPI(formProps.value.project);
    await fetchProjects();
    dialog.value = false;
}

async function updateProject() {
    await updateProjectAPI(formProps.value.project);
    await fetchProjects();
    dialog.value = false;
}

async function deleteProject() {
    await deleteProjectAPI(formProps.value.project.id);
    await fetchProjects();
    deleteDialog.value = false;
}

function handleClick(event, row) {
    const id = row.item.id;
    router.push({ path: `/projects/${id}/tasks` });
}

function openDeleteForm(project: Project) {
    formProps.value.project = { ...project };
    deleteDialog.value = true;
}

function closeDeleteForm() {
    deleteDialog.value = false;
}

onMounted(fetchProjects);
</script>
