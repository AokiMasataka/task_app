<template>
    <div style="height: 60vh" class="overflow-scroll">
        <Markdown
            v-if="isPreviewMode"
            :content="content"
        />
        <v-textarea
            v-else
            v-model="content"
            label="Content*"
            rows="24"
            required
            auto-grow
            variant="solo-filled"
            hide-details="true"
        />
    </div>
</template>

<script setup lang="ts">
import Markdown from './Markdown.vue';

const content = defineModel<string>("content", { required: true });
const isPreviewMode = defineModel<boolean>("isPreviewMode", {required: true});
</script>