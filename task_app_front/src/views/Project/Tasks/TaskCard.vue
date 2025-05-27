<template>
    <ItemCard
        :id="props.task.id"
        :title="props.task.title"
        :subtitle="props.task.content"
        :draggable="true"
        @fetch-item="$emit('onFecthTask')"
        @update-item="$emit('onUpdateTask')"
        @delete-item="$emit('onDeleteTask')"
        @dragstart="$emit('onDragStart')"
        @dragend="$emit('onDragEnd')"
    />
</template>

<script setup lang="ts">
import ItemCard from "@/components/ItemCard";
import { Task } from "@/scripts/types";

const props = defineProps<{ task: Task }>();
defineEmits<{
    (e: "onFecthTask"): void;
    (e: "onUpdateTask"): void;
    (e: "onDeleteTask"): void;
    (e: "onDragStart"): void;
    (e: "onDragEnd"): void;
}>();

function isEmptyContent(content: string): string {
    if (content == "") {
        return "no content";
    } else {
        return content;
    }
}
</script>
