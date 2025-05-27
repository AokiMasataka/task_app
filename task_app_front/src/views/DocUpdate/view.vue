<template>
    <DocForm
        createOrUpdate="UPDATE"
        @on-submit="updateDoc"
        @back="back"
        v-model="doc"
    />
</template>

<script setup lang="ts">
import DocForm from "@/components/forms/DocForm.vue";
import { fetchDocAPI, updateDocAPI } from "@/scripts/docApi";
import { Doc } from "@/scripts/types";
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";

const router = useRouter();
const projectId = useRoute().params.projectId as string;
const docId = useRoute().params.docId as string;

const doc = ref<Doc>({ id: "", project_id: "", title: "", content: "" });

async function fetchDoc() {
    doc.value = await fetchDocAPI(projectId, docId);
}

async function updateDoc() {
    await updateDocAPI(projectId, doc.value);
    router.push({ path: `/projects/${projectId}/docs/${docId}` });
}

function back() {
    router.push({ path: `/projects/${projectId}/docs/${docId}` });
}

onMounted(fetchDoc);
</script>
