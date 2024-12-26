<template>
    <v-tooltip>
        <template  v-slot:activator="{ props }">
            <v-icon
                v-bind="props"
                class="pt-1"
                @click="$emit('onUpdate')">
                mdi-pencil
            </v-icon>
        </template>
        <span>update</span>
    </v-tooltip>
</template>

<script setup lang="ts">

defineEmits<{(e: 'onUpdate'): void}>();
</script>