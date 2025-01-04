<template>
    <div class="relative group">
        <v-card
            class="my-2 mx-4 group-hover:bg-neutral-800"
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

        <v-card
            density="compact"
            class="absolute -top-5 right-6 invisible group-hover:visible bg-neutral-700"
        >
            <div class="mx-1 my-1 flex gap-x-1.5">
                <UpdateBtn
                    @on-update="$emit('handleFecthTask', props.task.id)"
                />

                <DeleteBtn
                    @on-delete="$emit('onDelete')"
                />
            </div>
        </v-card>
    </div>
</template>

<script setup lang="ts">
import { Task } from '../../scripts/types';
import DeleteBtn from '../common/DeleteBtn.vue';
import UpdateBtn from '../common/UpdateBtn.vue';

const props = defineProps<{task: Task}>();
defineEmits<{
    (e: 'handleFecthTask', task_id: string): unknown,
    (e: 'onDragStart', task: Task): unknown,
    (e: 'onDragEnd'): unknown,
    (e: 'onDelete'): unknown
}>();

function isEmptyContent(content: string): string {
    if (content == "") {
        return "no content"
    } else {
        return content;
    };
};
</script>
