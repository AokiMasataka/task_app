<template>
    <v-text-field
        v-model="title"
        variant="solo-filled"
        placeholder="input title"
        required
        :rules="[rules.required]"
    />
</template>

<script setup lang="ts">
const title = defineModel<string>("title", { required: true });

const rules = {required: value => !!value || 'Field is required'}
</script>