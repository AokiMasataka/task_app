<template>
    <v-tooltip>
        <template  v-slot:activator="{ props }">
            <v-icon
                v-bind="props"
                class="pt-1"
                color="red"
                @click="model = true">
                mdi-delete
            </v-icon>
        </template>
        <span>delete</span>
    </v-tooltip>

    <v-dialog v-model="model" max-width="600">
        <v-card title="Delete Task?">
            <v-card-actions>
                <v-btn
                    text="Cancel"
                    variant="plain"
                    @click="model = false"
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

const model = defineModel<boolean>({ required: true });
defineEmits<{
    (e: 'onDelete'): void,
}>();
</script>