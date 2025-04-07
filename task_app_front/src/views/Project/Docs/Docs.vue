<template>
    <div>
        <div v-for="doc in docs">
            <ItemCard
                :id="doc.id"
                :title="doc.title"
                :subtitle="doc.content"
                @fetch-item="viewDoc(doc.id)"
                @update-item="updateDoc(doc.id)"
                @delete-item="deleteDoc(doc.id)"
            />
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import ItemCard from "@/components/ItemCard";
import { fetchDocsAPI, deleteDocAPI } from "@/scripts/docApi";
import { Docs } from "@/scripts/types";

const router = useRouter();
const projectId = useRoute().params.projectId as string;

const docs = ref<Docs>([]);

async function fetchDocs() {
    const results = await fetchDocsAPI(projectId);
    docs.value = results.results;
}

function viewDoc(docId: string) {
    router.push({ path: `/projects/${projectId}/docs/${docId}` });
}

function updateDoc(docId: string) {
    router.push({ path: `/projects/${projectId}/docs/${docId}/edit` });
}

async function deleteDoc(docId: string) {
    await deleteDocAPI(projectId, docId);
    await fetchDocs();
}

onMounted(fetchDocs);
</script>
