<template>
    <v-btn @click="$emit('onClick')">+</v-btn>
</template>

<script setup lang="ts">
defineEmits<{(e: 'onClick'): void}>();
</script>