<template>
    <ItemCard
        :draggable="true"
        @fetch-item="$emit('onFecthTask')"
        @update-item="$emit('onUpdateTask')"
        @delete-item="$emit('onDeleteTask')"
        @dragstart="$emit('onDragStart')"
        @dragend="$emit('onDragEnd')"
    >
        <v-card-item>
            <v-card-title>{{ props.task.title }}</v-card-title>
            <v-card-subtitle>
                <div class="flex h-4 items-center">
                    <component
                        :is="prefixIcon(props.task.duedate)"
                        class="h-full"
                    />

                    {{ dateStringify(props.task.duedate) }}
                </div>
            </v-card-subtitle>
        </v-card-item>
    </ItemCard>
</template>

<script setup lang="ts">
import ItemCard from "@/components/ItemCard";
import IconWarn from "@/components/icons/Warn.vue";
import { dateToString } from "@/scripts/date";
import { Task } from "@/scripts/types";

const props = defineProps<{ task: Task }>();

defineEmits<{
    (e: "onFecthTask"): void;
    (e: "onUpdateTask"): void;
    (e: "onDeleteTask"): void;
    (e: "onDragStart"): void;
    (e: "onDragEnd"): void;
}>();

function prefixIcon(date: Date | null) {
    if (date === null) {
        return null;
    }

    const now = new Date();
    now.setHours(date.getHours(), 0, 0, 0);
    // 当日
    if (date >= now) {
        return IconWarn;
    }

    return null;
}

function dateStringify(data: Date | null): string {
    if (data == null) {
        return "no duedate";
    } else {
        return dateToString(data);
    }
}

function isEmptyContent(content: string): string {
    if (content == "") {
        return "no content";
    } else {
        return content;
    }
}
</script>
