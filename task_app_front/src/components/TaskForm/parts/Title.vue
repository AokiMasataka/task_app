<template>
    <div v-if="isPreviewMode">{{ title }}</div>
    <v-text-field
        v-else
        v-model="title"
        variant="solo-filled"
        placeholder="input title"
        required
        :rules="[rules.required]"
    />
</template>

<script setup lang="ts">
const isPreviewMode = defineModel<boolean>("isPreviewMode", { required: true });
const title = defineModel<string>("title", { required: true });

const rules = {required: value => !!value || 'Field is required'}
</script>