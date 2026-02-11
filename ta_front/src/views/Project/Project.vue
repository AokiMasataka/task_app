<template>
    <Header></Header>
    <Sidebar></Sidebar>
    <div class="mx-8">
        <h1 class="text-3xl my-4">{{ projectName }}</h1>
        <SwitchTab :project-id="projectId">
            <template v-slot:tasks><Tasks /></template>
            <template v-slot:docs><Docs /></template>
        </SwitchTab>
    </div>
</template>

<script setup lang="ts">
import Header from '@/components/Header';
import Sidebar from '@/components/Sidebar';
import { fetchProjectAPI } from "@/scripts/projectApi";
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import SwitchTab from "./SwitchTab.vue";

import Docs from "./Docs/Docs.vue";
import Tasks from "./Tasks/Tasks.vue";

const route = useRoute();
const projectId = route.params.projectId as string;

const projectName = ref<string>("");

async function fetchProjectName() {
    projectName.value = (await fetchProjectAPI(projectId)).title;
}

onMounted(fetchProjectName);
</script>
