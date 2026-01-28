<template>
    <div class="flex justify-between">
        <v-tabs :model-value="tabName">
            <v-tab value="tasks" @click="onTasksClick">tasks</v-tab>
            <v-tab value="docs" @click="onDocsClick">docs</v-tab>
        </v-tabs>
    </div>

    <v-window :model-value="tabName">
        <v-window-item
            value="tasks"
            transition="none"
            reverse-transition="none"
        >
            <slot name="tasks"> </slot>
        </v-window-item>
        <v-window-item value="docs" transition="none" reverse-transition="none">
            <slot name="docs"> </slot>
        </v-window-item>
    </v-window>

    <div class="mt-4">
        <slot> </slot>
    </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { useRoute, useRouter } from "vue-router";

const router = useRouter();
const route = useRoute();

const props = defineProps<{ projectId: string }>();

const tabName = computed(() => {
    return route.params.tabName;
});

function onTasksClick() {
    router.push({ path: `/projects/${props.projectId}/tasks` });
}

function onDocsClick() {
    router.push({ path: `/projects/${props.projectId}/docs` });
}

function onCreateDoc() {
    router.push({ path: `/projects/${props.projectId}/docs/new` });
}
</script>
