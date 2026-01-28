<template>
    <div class="mx-8 my-4">
        <div class="flex gap-4 justify-between">
            <v-btn clas="mt-4" @click="back">Back</v-btn>
            <div class="flex gap-4">
                <v-btn @click="switchViewMode">Switch view mode</v-btn>
                <v-btn
                    :color="valid ? 'primary' : 'grey-darken-1'"
                    text="Save"
                    variant="tonal"
                    @click="updateDoc"
                    :readonly="!valid"
                    >Create</v-btn
                >
            </div>
        </div>
        <div>
            <Title class="mt-4" v-model:title="doc.title" />
            <Content
                class=""
                v-model:isPreviewMode="isPreviewMode"
                v-model:content="doc.content"
            />
        </div>
    </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import Content from "../components/atomic/Content.vue";
import Title from "../components/atomic/Title.vue";
import { fetchDocAPI, updateDocAPI } from "../scripts/docApi";
import { Doc } from "../scripts/types";

const router = useRouter();
const projectId = useRoute().params.projectId as string;
const docId = useRoute().params.docId as string;

const isPreviewMode = ref<boolean>(false);
const doc = ref<Doc>({ id: "", project_id: "", title: "", content: "" });

async function updateDoc() {
    await updateDocAPI(projectId, doc.value);
    router.push({ path: `/projects/${projectId}/docs/${docId}` });
}

async function fetchDoc() {
    doc.value = await fetchDocAPI(projectId, docId);
}

function switchViewMode() {
    isPreviewMode.value = !isPreviewMode.value;
}

function back() {
    router.push({ path: `/projects/${projectId}/docs` });
}

const valid = computed(() => {
    return doc.value.title != "";
});

onMounted(fetchDoc);
</script>
