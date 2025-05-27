<template>
    <v-tooltip location="top">
        <template v-slot:activator="{ props }">
            <v-icon
                :icon="IconPencil"
                v-bind="props"
                class="pt-1"
                @click.stop="$emit('onUpdate')"
            >
            </v-icon>
        </template>
        <span>update</span>
    </v-tooltip>
</template>

<script setup lang="ts">
import IconPencil from "@/components/icons/Pencil.vue";

defineEmits<{ (e: "onUpdate"): void }>();
</script>
