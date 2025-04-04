<template>
    <div class="mx-8 my-4">
        <h1 class="text-3xl my-4">{{ ProjectName }}</h1>
        <div class="flex justify-between">
            <TabSwitch />
            <v-btn class="" @click="onCreateDoc">Create New Doc</v-btn>
        </div>

        <div v-for="doc in docs">
            <v-card
                class="mt-4"
                :title="doc.title"
                :subtitle="doc.content"
                @click="viewDoc(doc.id)"
            />
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import TabSwitch from "../../../components/TabSwitch";
import { fetchDocsAPI } from "../../../scripts/docApi";
import { Docs } from "../../../scripts/types";

const router = useRouter();
const projectId = useRoute().params.projectId as string;
const ProjectName = "Sample Project";

const docs = ref<Docs>([]);

async function fetchDocs() {
    const results = await fetchDocsAPI(projectId);
    docs.value = results.results;
}

function viewDoc(docId: string) {
    router.push({ path: `/projects/${projectId}/docs/${docId}` });
}

function onCreateDoc() {
    router.push({ path: `/projects/${projectId}/docs/new` });
}

onMounted(fetchDocs);
</script>
