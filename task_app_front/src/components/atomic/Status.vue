<template>
    <v-select
        v-model="status"
        :items="items"
        item-title="text"
        item-value="value"
        label="status"
        variant="underlined"
        hide-details="auto"
    />
</template>

<script setup lang="ts">
// import { items } from '../const';
import { state } from "../../scripts/const";

const items = Object.entries(state).map(([text, value]) => {
    return {
        text,
        value,
    };
});

const status = defineModel<number>("status", { required: true });
</script>
