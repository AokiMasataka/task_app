<template>
    <div style="height: 60vh" class="overflow-auto">
        <div
            class="src-components-TaskForm-Markdown mx-2"
            v-html="markdown"
        ></div>
    </div>
</template>
<script setup lang="ts">
import { marked } from "marked";
import { ref, watch } from "vue";

const props = defineProps<{ content: string }>();
const markdown = ref<string>("");

watch(
    () => props.content,
    async (newContent) => {
        markdown.value = await marked(newContent || "");
    },
    { immediate: true } // 初回描画時にも実行
);
</script>

<style lang="css">
.src-components-TaskForm-Markdown h1 {
    font-size: 3.75rem;
    line-height: 1;
    margin: 1rem 0;
}
.src-components-TaskForm-Markdown h2 {
    font-size: 3rem;
    line-height: 1;
    margin: 1rem 0;
}
.src-components-TaskForm-Markdown h3 {
    font-size: 2.25rem; /* 36px */
    line-height: 2.5rem;
    margin: 1rem 0;
}
.src-components-TaskForm-Markdown h4 {
    font-size: 1.875rem; /* 30px */
    line-height: 2.25rem; /* 36px */
    margin: 1rem 0;
}
.src-components-TaskForm-Markdown h5 {
    font-size: 1.5rem; /* 24px */
    line-height: 2rem; /* 32px */
    margin: 1rem 0;
}
.src-components-TaskForm-Markdown h6 {
    font-size: 1.25rem; /* 20px */
    line-height: 1.75rem; /* 28px */
    margin: 1rem 0;
}

.src-components-TaskForm-Markdown ul {
    list-style-type: disc;
    margin-left: 16px;
}

.src-components-TaskForm-Markdown ol {
    list-style-type: decimal;
    margin-left: 16px;
}
</style>
