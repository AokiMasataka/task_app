<template>
    <div class="mx-8">
        <h1 class="text-3xl my-4">{{ ProjectName }}</h1>
        <SwitchTab
        :project-id="projectId"/>
    </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router';
import SwitchTab from './SwitchTab.vue';

const route = useRoute()

const ProjectName = "Sample Project";
const projectId = route.params.projectId as string;
</script>