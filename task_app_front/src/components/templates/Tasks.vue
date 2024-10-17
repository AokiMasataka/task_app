<template>
    <div class="w-1/3 h-4/5 bg-neutral-700 ml-8 mt-4 rounded-md">
        <div class="flex items-center justify-between">
            <h1 class="m-6 text-2xl">{{ props.displayStatus }}</h1>
            <AddTaskBtn
                class="m-4"
                @on-click="handleAddTaskBtn"
            />
        </div>
        
        <v-card
            class="my-2 mx-4"
            v-for="task in props.tasks"
            :title="task.title"
            :subtitle="isEmptyContent(task.content)"
            @click="handleFecthTask(task.id)"
        >
        </v-card>

        <v-dialog v-model="isActivateForm" max-width="600">
            <TaskForm
                v-model="formProps.initTaskData"
                :is-update-form="formProps.isUpdateForm"
                @on-close="isActivateForm = false"
                @on-save="formProps.onSave"
                @on-delete="formProps.onDelete"
            />
        </v-dialog>
    </div>
</template>

<script setup lang="ts">
import {
    fetchTaskAPI
} from '@/scripts/taskApi';
import { Task, Tasks } from '@/scripts/types';
import { ref } from 'vue';
import AddTaskBtn from '../common/AddTaskBtn.vue';
import TaskForm from '../common/TaskForm.vue';


const CreateInitTaskData = (): Task => {
    return {
        title: "",
        content: "",
        id: "",
        status: props.valueStatus
    };
};

const props = defineProps<{
    displayStatus: string,
    valueStatus: number,
    tasks: Tasks,
}>();
const emit = defineEmits<{
    (e: 'createTask', task: Task): unknown,
    (e: 'updateTask', task: Task): unknown,
    (e: 'deleteTask', id: string): unknown
}>();

const isActivateForm = ref<boolean>(false);
const formProps = ref<{
    initTaskData: Task,
    isUpdateForm: boolean,
    onSave: () => unknown,
    onDelete: ()=> Promise<void>,
}>({
    initTaskData: CreateInitTaskData(),
    isUpdateForm: true,
    onSave: async () => {},
    onDelete: async () => {},
});

function handleAddTaskBtn() {
    isActivateForm.value = true;
    formProps.value.initTaskData = CreateInitTaskData();
    formProps.value.isUpdateForm = false;
    formProps.value.onSave = async () => {
        emit('createTask', formProps.value.initTaskData);
        isActivateForm.value = false;
    };
    formProps.value.onDelete = async () => {};
};

async function handleFecthTask(task_id: string) {
    isActivateForm.value = true;
    formProps.value.initTaskData = await fetchTaskAPI(task_id);
    formProps.value.isUpdateForm = true;
    formProps.value.onSave = async () => {
        emit('updateTask', formProps.value.initTaskData);
        isActivateForm.value = false;
    };
    formProps.value.onDelete = async () => {
        emit('deleteTask', formProps.value.initTaskData.id);
        isActivateForm.value = false;
    };
};

function isEmptyContent(content: string) {
    if (content == "") {
        return "no content"
    } else {
        return content;
    };
};

</script>