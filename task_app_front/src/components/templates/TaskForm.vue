<template>
    <v-card>
        <v-card-title
            class="m-4 flex justify-between"
        >
            {{ formTitle }}
            <DeleteBtn v-if="props.isUpdateForm"
                v-model="isOpenConfirmDialog"
                @on-delete="$emit('onDelete')"
            />
        </v-card-title>

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
        <v-card-actions class="px-6">
            <v-btn
                text="Close"
                variant="plain"
                @click="$emit('onClose')"
            />
            <v-btn
                color="primary"
                text="Save"
                variant="tonal"
                @click="$emit('onSave')"
            />
        </v-card-actions>
    </v-card>
</template>

<script setup lang="ts">
import { items } from '@/scripts/const';
import { Task } from '@/scripts/types';
import { computed, ref } from 'vue';
import DeleteBtn from '../common/DeleteBtn.vue';

const props = defineProps<{isUpdateForm: boolean}>();
const model = defineModel<Task>({ required: true });
defineEmits<{
    (e: 'onClose'): void,
    (e: 'onSave'): void,
    (e: 'onDelete'): void,
}>();

const isOpenConfirmDialog = ref<boolean>(false);


const formTitle = computed(() => {
    return props.isUpdateForm ?  "Update Task" : "Create Task";
});

</script>
