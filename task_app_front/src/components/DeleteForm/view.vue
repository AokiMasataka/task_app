<template>
    <v-card :title="props.title">
        <v-card-actions>
            <v-btn text="Cancel" variant="plain" @click="$emit('onClose')" />

            <v-btn
                color="red"
                text="Delete"
                variant="tonal"
                @click="$emit('onDelete')"
            />
        </v-card-actions>
    </v-card>
</template>

<script setup lang="ts">
const props = defineProps<{ title: string }>();

defineEmits<{
    (e: "onDelete"): void;
    (e: "onClose"): void;
}>();
</script>
