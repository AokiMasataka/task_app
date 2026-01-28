<template>
    <DocForm
        createOrUpdate="CREATE"
        @on-submit="postDoc"
        @back="back"
        v-model="doc"
    />
</template>

<script setup lang="ts">
import DocForm from "@/components/forms/DocForm.vue";
import { postDocAPI } from "@/scripts/docApi";
import { Doc } from "@/scripts/types";
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";

const router = useRouter();
const projectId = useRoute().params.projectId as string;

const doc = ref<Doc>({ id: "", project_id: "", title: "", content: "" });

async function postDoc() {
    const docid = await postDocAPI(projectId, doc.value);
    router.push({ path: `/projects/${projectId}/docs/${docid.id}` });
}

function back() {
    router.push({ path: `/projects/${projectId}/docs` });
}
</script>
