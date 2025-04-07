<template>
    <div class="relative group">
        <v-card
            class="group-hover:bg-neutral-800"
        >
            <v-card-item>
                <v-card-title>
                    <span
                        @click="$emit('fetchItem')"
                        style="cursor: pointer"
                    >
                        {{ props.title }}
                    </span>
                </v-card-title>
                <v-card-subtitle>
                    {{ isEmptyContent(props.subtitle) }}
                </v-card-subtitle>
            </v-card-item>
        </v-card>

        <v-card
            density="compact"
            class="absolute -top-5 right-6 invisible group-hover:visible bg-neutral-700"
        >
            <div class="mx-1 my-1 flex gap-x-1.5">
                <UpdateBtn
                    @on-update="$emit('updateItem')"
                />

                <DeleteBtn
                    title="Delete Item?"
                    @on-delete="$emit('deleteItem')"
                />
            </div>
        </v-card>
    </div>
</template>

<script setup lang="ts">
import DeleteBtn from "@/components/DeleteBtn";
import UpdateBtn from "@/components/UpdateBtn";

const props = defineProps<{ id: string, title: string, subtitle: string}>();
defineEmits<{
    (e: "fetchItem"): unknown;
    (e: "updateItem"): unknown;
    (e: "deleteItem"): unknown;
}>();

function isEmptyContent(content: string): string {
    if (content == "") {
        return "no content";
    } else {
        return content;
    }
}
</script>
