<template>
    <div class="mx-8 my-4">
        <div class="flex gap-4 justify-between">
            <v-btn clas="mt-4" @click="$emit('back')">Back</v-btn>
            <BackBtn @on-back="$emit('back')" />
            <div class="flex gap-4">
                <v-btn @click="switchViewMode">Switch view mode</v-btn>
                <v-btn
                    :color="valid ? 'primary' : 'grey-darken-1'"
                    text="Save"
                    variant="tonal"
                    @click="$emit('onSubmit')"
                    :readonly="!valid"
                    >{{
                        props.createOrUpdate == "CREATE" ? "create" : "update"
                    }}
                </v-btn>
            </div>
        </div>
        <div>
            <Title class="mt-4" v-model:title="doc.title" />
            <Content
                class=""
                v-model:isPreviewMode="isPreviewMode"
                v-model:content="doc.content"
            />
        </div>
    </div>
</template>

<script setup lang="ts">
import BackBtn from "@/components/buttons/Back.vue";
import Content from "@/components/atomic/Content.vue";
import Title from "@/components/atomic/Title.vue";
import { Doc } from "@/scripts/types";
import { computed, ref } from "vue";

const isPreviewMode = ref<boolean>(false);

const doc = defineModel<Doc>({ required: true });
defineEmits<{
    (e: "back"): void;
    (e: "onSubmit"): void;
}>();

const props = defineProps<{
    createOrUpdate: "CREATE" | "UPDATE";
    likes?: number;
}>();

function switchViewMode() {
    isPreviewMode.value = !isPreviewMode.value;
}

const valid = computed(() => {
    return doc.value.title != "";
});
</script>
