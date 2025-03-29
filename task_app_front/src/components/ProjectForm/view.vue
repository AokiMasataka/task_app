<template>
    <v-card :title="props.title">
        <v-card-text>
            <v-text-field
                v-model="project.title"
                label="Project title"
                variant="solo-filled"
                placeholder="input title"
                required
                :rules="[rules.required]"
            />
            <v-text-field
                v-model="project.description"
                label="Project title"
                variant="solo-filled"
                placeholder="input title"
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
import { Project } from "../../scripts/types";

const props = defineProps<{ title: string }>();
const project = defineModel<Project>({ required: true });
defineEmits<{
    (e: "onClose"): void;
    (e: "onSave"): void;
}>();

const rules = { required: (value) => !!value || "Field is required" };
</script>
