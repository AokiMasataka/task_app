<template>
    <div class="grid grid-cols-2 gap-4 w-64">
        <v-btn
            class="border-t-2 border-x-2 border-indigo-600"
            @click="onTasksClick"
            >Tasks</v-btn
        >
        <v-btn
            class="border-t-2 border-x-2 border-indigo-600"
            @click="onDocsClick"
            >Docs</v-btn
        >
    </div>
</template>

<script setup lang="ts">
import { useRoute, useRouter } from "vue-router";

const projectId = useRoute().params.projectId as string;
const router = useRouter();

function onTasksClick() {
    router.push({ path: `/projects/${projectId}/tasks` });
}

function onDocsClick() {
    router.push({ path: `/projects/${projectId}/docs` });
}
</script>
