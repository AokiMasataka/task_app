<template>
    <div v-if="isPreviewMode">
        aaa
    </div>
    <v-select
        v-else
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
import { items } from '../const';

const isPreviewMode = defineModel<boolean>("isPreviewMode", { required: true });
const status = defineModel<number>("status", { required: true });
</script>