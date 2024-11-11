<template>
    <v-card :title="formTitle">
        <v-select
            class="mx-6"
            v-if="props.isUpdateForm"
            v-model="model.status"
            :items="items"
            item-title="text"
            item-value="value"
        />
        <v-card-text>
            <v-text-field
                v-model="model.title"
                label="Task Title*"
                required
            />
            <v-textarea
                v-model="model.content"
                label="Content*"
                rows="24"
                required
            />
        </v-card-text>
        <v-divider />
        <v-card-actions>
            <v-btn
                text="Close"
                variant="plain"
                @click="$emit('onClose')"
            />
            <v-btn
                color="#5865f2"
                text="Save"
                variant="tonal"
                @click="$emit('onSave')"
            />
            <v-btn
                v-if="props.isUpdateForm"
                color="red"
                text="Delete"
                variant="tonal"
                @click="$emit('onDelete')"
            />
        </v-card-actions>
    </v-card>
</template>

<script setup lang="ts">
import { items } from '@/scripts/const';
import { Task } from '@/scripts/types';
import { computed } from 'vue';

const props = defineProps<{isUpdateForm: boolean}>();
const model = defineModel<Task>({ required: true });
defineEmits<{
    (e: 'onClose'): void,
    (e: 'onSave'): void,
    (e: 'onDelete'): void,
}>();


const formTitle = computed(() => {
    return props.isUpdateForm ?  "Update Task" : "Create Task";
});

</script>
