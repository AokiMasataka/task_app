<template>
    <div class="flex flex-col">
        <div class="flex justify-end">
            <v-btn @click="onCreateDoc">Create New Doc</v-btn>
        </div>
        <div v-for="doc in docs" v-if="!isLoading" class="mt-2">
            <ItemCard
                :draggable="false"
                @fetch-item="viewDoc(doc.id)"
                @update-item="updateDoc(doc.id)"
                @delete-item="deleteDoc(doc.id)"
            >
                <v-card-item>
                    <v-card-title>{{ doc.title }}</v-card-title>
                    <v-card-subtitle>
                        <div class="flex h-4 items-center">
                            {{ doc.content }}
                        </div>
                    </v-card-subtitle>
                </v-card-item>
            </ItemCard>
        </div>

        <div v-else class="flex justify-center items-center">
            <v-progress-circular indeterminate />
        </div>
    </div>
</template>

<script setup lang="ts">
import ItemCard from "@/components/ItemCard";
import { deleteDocAPI, fetchDocsAPI } from "@/scripts/docApi";
import { Docs } from "@/scripts/types";
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";

const router = useRouter();
const projectId = useRoute().params.projectId as string;

const docs = ref<Docs>([]);
const isLoading = ref<boolean>(false);

async function fetchDocs() {
    isLoading.value = true;
    try {
        const results = await fetchDocsAPI(projectId);
        docs.value = results.results;
    } finally {
        isLoading.value = false;
    }
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

function onCreateDoc() {
    router.push({ path: `/projects/${projectId}/docs/new` });
}

onMounted(fetchDocs);
</script>
