<template>
    <div class="mx-8 my-4">
        <v-btn class="my-4" @click="dialog = true">New Project</v-btn>

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
                    <v-icon
                        :icon="Pencil"
                        @click.stop="console.log(item.title)"
                    />
                    <v-icon
                        :icon="Trash"
                        @click.stop="console.log(item.title)"
                    />
                </div>
            </template>
        </v-data-table-server>

        <v-dialog v-model="dialog" width="800">
            <v-card title="aaaaa">
                <v-text-field
                    v-model="createProjectProps.title"
                    variant="solo-filled"
                    placeholder="input title"
                    required
                />
            </v-card>
        </v-dialog>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import Pencil from "../components/icons/Pencil.vue";
import Trash from "../components/icons/Trash.vue";
import {
    createProjectAPI,
    deleteProjectAPI,
    fetchProjectsAPI,
} from "../scripts/projectApi";
import { Project, Projects } from "../scripts/types";

const itemsPerPage = ref(5);
const loading = ref(false);
const router = useRouter();
const projects = ref<Projects>([]);

const dialog = ref<boolean>(false);
const createProjectProps = ref<Project>({ id: "", title: "", description: "" });

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

async function cretaeProject() {
    await createProjectAPI(createProjectProps.value);
    await fetchProjects();
}

async function deleteProject() {
    await deleteProjectAPI("aa");
    await fetchProjects();
}

function handleClick(event, row) {
    const id = row.item.id;
    router.push({ path: `/projects/${id}/tasks` });
}

function clickEdit(item: Project) {}

onMounted(fetchProjects);
</script>
