<template>
    <div class="relative group">
        <v-card
            class="group-hover:bg-neutral-800 cursor-pointer"
            :draggable="props.draggable"
            :ripple="false"
            @click="$emit('fetchItem')"
        >
            <slot></slot>
        </v-card>

        <v-card
            density="compact"
            class="absolute -top-5 right-6 invisible group-hover:visible bg-neutral-700"
        >
            <div class="mx-1 my-1 flex gap-x-1.5">
                <UpdateBtn @on-update="$emit('updateItem')" />

                <DeleteBtn
                    title="Delete Item?"
                    @on-delete="$emit('deleteItem')"
                />
            </div>
        </v-card>
    </div>
</template>

<script setup lang="ts">
import DeleteBtn from "@/components/buttons/Delete.vue";
import UpdateBtn from "@/components/buttons/Update.vue";

const props = defineProps<{
    draggable: boolean;
}>();
defineEmits<{
    (e: "fetchItem"): void;
    (e: "updateItem"): void;
    (e: "deleteItem"): void;
}>();

function isEmptyContent(content: string): string {
    if (content == "") {
        return "no content";
    } else {
        return content;
    }
}
</script>
