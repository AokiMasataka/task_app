<template>
    <v-card :title="props.title">
        <v-card-text>
            <Title v-model:title="project.title" />
            <v-text-field
                v-model="project.description"
                label="Project title"
                variant="solo-filled"
                placeholder="description"
                required
            />
        </v-card-text>
        <v-card-actions class="px-8">
            <v-btn text="Close" variant="plain" @click="$emit('onClose')" />
            <v-btn
                color="primary"
                text="Save"
                variant="tonal"
                @click="$emit('onSave')"
            />
        </v-card-actions>
    </v-card>
</template>

<script setup lang="ts">
import Title from "@/components/atomic/Title.vue";
import { Project } from "@/scripts/types";

const props = defineProps<{ title: string }>();
const project = defineModel<Project>({ required: true });
defineEmits<{
    (e: "onClose"): void;
    (e: "onSave"): void;
}>();
</script>
