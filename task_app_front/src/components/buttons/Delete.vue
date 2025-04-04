<template>
    <v-tooltip location="top">
        <template v-slot:activator="{ props }">
            <v-icon
                :icon="IconDelete"
                v-bind="props"
                class="pt-1"
                @click.stop="deleteDialog = true"
            >
            </v-icon>
        </template>
        <span>delete</span>
    </v-tooltip>

    <v-dialog v-model="deleteDialog" max-width="600">
        <DeleteForm
            :title="props.title"
            @on-delete="$emit('onDelete')"
            @on-close="deleteDialog = false"
        />
    </v-dialog>
</template>

<script setup lang="ts">
import DeleteForm from "@/components/forms/DeleteForm.vue";
import IconDelete from "@/components/icons/Trash.vue";

import { ref } from "vue";
const props = defineProps<{ title: string }>();

const deleteDialog = ref<boolean>(false);
defineEmits<{ (e: "onDelete"): void }>();
</script>
