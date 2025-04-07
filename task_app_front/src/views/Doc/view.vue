<template>
    <div class="mx-8 my-4">
        <div class="flex justify-between">
            <v-btn @click="back">Back</v-btn>
            <div class="flex gap-4">
                <v-btn @click="deleteDoc">delete</v-btn>
                <v-btn @click="update">edit</v-btn>
            </div>
        </div>

        <h1 class="text-5xl mt-4">{{ doc.title }}</h1>
        <hr class="my-4" />
        <MarkDown :key="doc.id" :content="doc.content" />
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import MarkDown from "@/components/atomic/MarkDown.vue";
import { deleteDocAPI, fetchDocAPI } from "@/scripts/docApi";
import { Doc } from "@/scripts/types";

const router = useRouter();
const projectId = useRoute().params.projectId as string;
const docId = useRoute().params.docId as string;

const doc = ref<Doc>({ id: "", project_id: "", title: "", content: "" });

async function fetchDoc() {
    doc.value = await fetchDocAPI(projectId, docId);
}

async function deleteDoc() {
    await deleteDocAPI(projectId, docId);
    back();
}

function update() {
    router.push({ path: `/projects/${projectId}/docs/${docId}/edit` });
}

function back() {
    router.push({ path: `/projects/${projectId}/docs` });
}

onMounted(fetchDoc);
</script>
