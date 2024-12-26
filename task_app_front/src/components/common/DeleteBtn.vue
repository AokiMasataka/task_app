<template>
    <v-tooltip location="top">
        <template  v-slot:activator="{ props }">
            <v-icon
                :icon="IconDelete"
                v-bind="props"
                class="pt-1"
                @click="deleteDialog = true">
                <!-- mdi-delete -->
            </v-icon>
        </template>
        <span>delete</span>
    </v-tooltip>

    <v-dialog v-model="deleteDialog" max-width="600">
        <v-card title="Delete Task?">
            <v-card-actions>
                <v-btn
                    text="Cancel"
                    variant="plain"
                    @click="deleteDialog = false"
                />

                <v-btn
                    color="red"
                    text="Delete"
                    variant="tonal"
                    @click="$emit('onDelete')"
                />
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import IconDelete from '../icons/Trash.vue';

const deleteDialog = ref<boolean>(false);
defineEmits<{(e: 'onDelete'): void}>();
</script>