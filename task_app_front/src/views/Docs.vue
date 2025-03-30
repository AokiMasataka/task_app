<template>
    <v-card>
        <v-card-text>
            <v-text-field
                v-model="doc.title"
                variant="solo-filled"
                placeholder="input title"
                required
            />
            <v-text-field
                v-model="doc.content"
                variant="solo-filled"
                placeholder="input title"
                required
            />
        </v-card-text>
        <v-card-actions>
            <v-btn
                @click="postDoc"
            >Save</v-btn>
        </v-card-actions>
    </v-card>

    <div v-for="doc in docs">
        <v-card
            class="m-4"
            :title="doc.title"
            :subtitle="doc.content"
        />
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router"
import { fetchDocsAPI, postDocAPI } from "../scripts/docApi";
import { Docs, Doc } from "../scripts/types";


const projectId = useRoute().params.projectId as string;
const docs = ref<Docs>([]);
const doc = ref<Doc>({id: "", project_id: "", title: "", content: ""});


async function fetchDocs() {
    const results = await fetchDocsAPI(projectId);
    docs.value = results.results;
};


async function postDoc() {
    await postDocAPI(projectId, doc.value);
    await fetchDocs();
    doc.value = {id: "", project_id: "", title: "", content: ""};
}

onMounted(fetchDocs);

</script>
