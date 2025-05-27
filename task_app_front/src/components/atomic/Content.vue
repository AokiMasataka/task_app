<template>
    <div style="height: 60vh" class="overflow-auto">
        <div
            v-if="isPreviewMode"
            class="src-components-TaskForm-Markdown mx-2"
            v-html="markdown"
        ></div>
        
        <div v-else class="grid grid-cols-2 gap-2">
            <v-textarea
                v-model="content"
                label="Content"
                rows="24"
                required
                auto-grow
                variant="solo-filled"
                hide-details="true"
                @input="perseMarkdown"
            />
            <div
                class="src-components-TaskForm-Markdown"
                v-html="markdown"
            ></div>
        </div>
    </div>

</template>
<script setup lang="ts">
import { marked } from 'marked';
import { onMounted, ref, watch } from 'vue';
const content = defineModel<string>("content", { required: true });
const isPreviewMode = defineModel<boolean>("isPreviewMode", {required: true});

const props = defineProps<{content: string}>();
const markdown = ref<string>("");

async function perseMarkdown (){
    markdown.value = await marked(props.content);
}

watch(() => isPreviewMode.value, () => {
    perseMarkdown()
});

onMounted(perseMarkdown);
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