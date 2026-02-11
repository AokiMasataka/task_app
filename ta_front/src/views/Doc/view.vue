<template>
    <Header></Header>
    <Sidebar></Sidebar>
    <div class="mx-8 my-4">
        <div class="flex justify-between">
            <BackBtn @on-back="back" />
            <div class="flex gap-4">
                <DeleteBtn title="Delete this Doc" @on-delete="deleteDoc" />
                <UpdateBtn @on-update="update" />
                <More
                    :items="[
                        { title: 'delete', func: deleteDoc, icon: IconDelete },
                        {
                            title: 'archive',
                            func: archiveDon,
                            icon: IconDelete,
                        },
                    ]"
                />
            </div>
        </div>

        <h1 class="text-5xl mt-4">{{ doc.title }}</h1>
        <hr class="my-4" />
        <MarkDown :key="doc.id" :content="doc.content" />
    </div>
</template>

<script setup lang="ts">
import Header from '@/components/Header';
import Sidebar from '@/components/Sidebar';
import MarkDown from "@/components/atomic/MarkDown.vue";
import BackBtn from "@/components/buttons/Back.vue";
import DeleteBtn from "@/components/buttons/Delete.vue";
import More from "@/components/buttons/More.vue";
import UpdateBtn from "@/components/buttons/Update.vue";
import IconDelete from "@/components/icons/Trash.vue";
import { deleteDocAPI, fetchDocAPI } from "@/scripts/docApi";
import { Doc } from "@/scripts/types";
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";

const router = useRouter();
const projectId = useRoute().params.projectId as string;
const docId = useRoute().params.docId as string;

const deleteDialog = ref<boolean>(false);
const doc = ref<Doc>({ id: "", project_id: "", title: "", content: "" });

async function fetchDoc() {
    doc.value = await fetchDocAPI(projectId, docId);
}

async function deleteDoc() {
    await deleteDocAPI(projectId, docId);
    back();
}

function deleteDialogClone() {
    deleteDialog.value = false;
}

function update() {
    router.push({ path: `/projects/${projectId}/docs/${docId}/edit` });
}

function back() {
    router.push({ path: `/projects/${projectId}/docs/` });
}

async function archiveDon() {
    alert("あとで実装します");
}

onMounted(fetchDoc);
</script>
