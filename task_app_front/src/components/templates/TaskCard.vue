<template>
    <v-card
        class="my-2 mx-4"
        draggable="true"
        @dragstart="$emit('onDragStart', props.task)"
        @dragend="$emit('onDragEnd')"
    >
        <v-card-item>
            <v-card-title>
                <span
                    @click="$emit('handleFecthTask', props.task.id)"
                    style="cursor: pointer"
                >
                    {{ props.task.title }}
                </span>
            </v-card-title>
            <v-card-subtitle>
                {{ isEmptyContent(props.task.content) }}
            </v-card-subtitle>
        </v-card-item>
    </v-card>
</template>

<script setup lang="ts">
import { Task } from '../../scripts/types';

const props = defineProps<{task: Task}>();
defineEmits<{
    (e: 'handleFecthTask', task_id: string): unknown
    (e: 'onDragStart', task: Task): unknown,
    (e: 'onDragEnd'): unknown
}>();

function isEmptyContent(content: string) {
    if (content == "") {
        return "no content"
    } else {
        return content;
    };
};

</script>