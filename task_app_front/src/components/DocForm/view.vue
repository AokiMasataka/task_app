<template>
    <v-card :title="props.title">
        <v-card-text>
            <Title v-model:title="doc.title" />
        </v-card-text>
        <v-card-actions></v-card-actions>
    </v-card>
</template>
<script setup lang="ts">
import { Doc } from "../../scripts/types";
import Title from "../atomic/Title.vue";

const props = defineProps<{ title: string }>();
const doc = defineModel<Doc>({ required: true });
defineEmits<{
    (e: "onClose"): void;
    (e: "onSave"): void;
}>();

const rules = { required: (value) => !!value || "Field is required" };
</script>
