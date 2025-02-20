<template>
    <v-tooltip location="top">
        <template  v-slot:activator="{ props }">
            <v-icon
                :icon="IconPencil"
                v-bind="props"
                class="pt-1"
                @click="$emit('onUpdate')">
            </v-icon>
        </template>
        <span>update</span>
    </v-tooltip>
</template>

<script setup lang="ts">
import IconPencil from '../icons/Pencil.vue';

defineEmits<{(e: 'onUpdate'): void}>();
</script>