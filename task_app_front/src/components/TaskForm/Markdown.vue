<template>
    <div v-html="markdown"></div>
</template>

<script setup lang="ts">
import { marked } from 'marked';

const props = defineProps<{content: string}>();
const markdown = marked(props.content);
</script>