<template>
    <v-card>
        <v-card-title class="m-4 flex justify-between">
            {{ formTitle }}
            <DeleteBtn
                v-if="props.isUpdateForm"
                title="Delete Task?"
                @on-delete="$emit('onDelete')"
            />
        </v-card-title>

        <div class="mx-8 mb-4 grid grid-cols-3 gap-8">
            <Status v-model:status="model.status" />
            <Priority v-model:priority="model.priority" />
            <Duedate v-model:duedate="model.duedate" />
        </div>

        <v-card-text>
            <Title v-model:title="model.title" />
            <Content
                v-model:isPreviewMode="isPreviewMode"
                v-model:content="model.content"
            />
        </v-card-text>

        <v-divider />
        <v-card-actions class="px-6">
            <v-btn text="switch mode" @click="isPreviewMode = !isPreviewMode" />
            <v-btn text="Close" variant="plain" @click="$emit('onClose')" />
            <v-btn
                :color="valid ? 'primary' : 'grey-darken-1'"
                text="Save"
                variant="tonal"
                @click="$emit('onSave')"
                :readonly="!valid"
            />
        </v-card-actions>
    </v-card>
</template>

<script setup lang="ts">
import Content from "@/components/atomic/Content.vue";
import Duedate from "@/components/atomic/Duedate.vue";
import Priority from "@/components/atomic/Priority.vue";
import Status from "@/components/atomic/Status.vue";
import Title from "@/components/atomic/Title.vue";
import DeleteBtn from "@/components/buttons/Delete.vue";
import { Task } from "@/scripts/types";
import { computed, ref } from "vue";

const props = defineProps<{ isUpdateForm: boolean; isPreviewMode: boolean }>();
const model = defineModel<Task>({ required: true });
defineEmits<{
    (e: "onClose"): void;
    (e: "onSave"): void;
    (e: "onDelete"): void;
}>();

const isPreviewMode = ref<boolean>(props.isPreviewMode);

const valid = computed(() => {
    return model.value.title != "";
});

const formTitle = computed(() => {
    return props.isUpdateForm ? "Update Task" : "Create Task";
});
</script>
