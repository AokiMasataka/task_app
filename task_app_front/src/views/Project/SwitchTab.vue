<template>
    <div class="flex justify-between">
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

        <div>
            <v-btn @click="onCreateDoc" v-if="!isTasks">Create New Doc</v-btn>
        </div>
    </div>

    <div class="mt-4">
        <Tasks
            v-if="isTasks"
        />
        <Docs
            v-else
        />
    </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import Docs from "./Docs/Docs.vue";
import Tasks from "./Tasks/Tasks.vue"

const router = useRouter();
const props = defineProps<{projectId: string}>();
const isTasks = ref<boolean>(true);

function onTasksClick() {
    isTasks.value = true;
}

function onDocsClick() {
    isTasks.value = false;
}

function onCreateDoc() {
    router.push({ path: `/projects/${props.projectId}/docs/new` });
}

</script>