<template>
    <div
        class="w-1/3 h-4/5 bg-neutral-700 rounded-md overflow-auto"
        :class="{
            'border-2': props.emphasislStatus,
            'border-rose-500': props.emphasislStatus,
        }"
        @drop="handleTaskDrop"
        @dragover="dragOver"
    >
        <div class="flex justify-between items-center">
            <h1 class="m-6 text-2xl">{{ props.displayStatus }}</h1>
            <v-btn class="m-4" @click="onCreateTaskBtn">+</v-btn>
        </div>

        <v-progress-linear
            :class="{ invisible: !props.loading }"
            color="primary"
            indeterminate
        ></v-progress-linear>

        <TaskCard
            v-for="task in props.tasks"
            class="mx-4 my-2"
            :task="task"
            @on-fecth-task="onFecthTask(task.id, true)"
            @on-update-task="onFecthTask(task.id, false)"
            @on-delete-task="$emit('deleteTask', task.id)"
            @on-drag-start="dragStart(task)"
            @on-drag-end="$emit('onDragEnd')"
        ></TaskCard>

        <v-dialog v-model="isActivateForm" max-width="1000">
            <TaskForm
                v-if="!isLoading"
                v-model="formProps.initTaskData"
                :is-update-form="formProps.isUpdateForm"
                :is-preview-mode="formProps.isPreviewMode"
                @on-close="isActivateForm = false"
                @on-save="formProps.onSave"
                @on-delete="formProps.onDelete"
            />
            <div v-else class="flex justify-center items-center">
                <v-progress-circular indeterminate />
            </div>
        </v-dialog>
    </div>
</template>

<script setup lang="ts">
import { fetchTaskAPI } from "@/scripts/taskApi";
import { CreateInitTaskData, Task, Tasks } from "@/scripts/types";
import { ref } from "vue";
import { useRoute } from "vue-router";
import TaskCard from "./TaskCard.vue";
import TaskForm from "./TaskForm.vue";

const projectId = useRoute().params.projectId as string;

const draggingModel = defineModel<Task | null>("draggingTask");
const props = defineProps<{
    displayStatus: string;
    valueStatus: number;
    tasks: Tasks;
    emphasislStatus: boolean;
    loading: boolean;
}>();
const emit = defineEmits<{
    (e: "createTask", task: Task): void;
    (e: "updateTask", task: Task): void;
    (e: "deleteTask", id: string): void;
    (e: "onDragOver"): void;
    (e: "onDropTask", task: Task): void;
    (e: "onDragEnd"): void;
}>();

const isLoading = ref<boolean>(false);
const isActivateForm = ref<boolean>(false);
const formProps = ref<{
    initTaskData: Task;
    isUpdateForm: boolean;
    isPreviewMode: boolean;
    onSave: () => Promise<void>;
    onDelete: () => Promise<void>;
}>({
    initTaskData: CreateInitTaskData(props.valueStatus),
    isUpdateForm: true,
    isPreviewMode: false,
    onSave: async () => {},
    onDelete: async () => {},
});

function dragStart(task: Task): void {
    draggingModel.value = task;
}

function dragOver(evt: DragEvent): void {
    evt.preventDefault();
    emit("onDragOver");
}

function handleTaskDrop(event: DragEvent): void {
    if (draggingModel.value == null) {
        return;
    }

    event.preventDefault();

    const updateParams = {
        id: draggingModel.value.id,
        project_id: draggingModel.value.project_id,
        title: draggingModel.value.title,
        content: draggingModel.value.content,
        status: props.valueStatus,
        priority: draggingModel.value.priority,
        duedate: draggingModel.value.duedate,
    };

    emit("onDropTask", updateParams);

    draggingModel.value = null;
}

function onCreateTaskBtn(): void {
    isActivateForm.value = true;
    formProps.value.initTaskData = CreateInitTaskData(props.valueStatus);
    formProps.value.isUpdateForm = false;
    formProps.value.isPreviewMode = false;
    formProps.value.onSave = async () => {
        emit("createTask", formProps.value.initTaskData);
        isActivateForm.value = false;
    };
    formProps.value.onDelete = async () => {};
}

async function onFecthTask(
    task_id: string,
    isPreviewMode: boolean
): Promise<void> {
    isLoading.value = true;
    isActivateForm.value = true;

    try {
        formProps.value.initTaskData = await fetchTaskAPI(projectId, task_id);
    } finally {
        isLoading.value = false;
    }

    formProps.value.isUpdateForm = true;
    formProps.value.isPreviewMode = isPreviewMode;
    formProps.value.onSave = async () => {
        emit("updateTask", formProps.value.initTaskData);
        isActivateForm.value = false;
    };
    formProps.value.onDelete = async () => {
        emit("deleteTask", formProps.value.initTaskData.id);
        isActivateForm.value = false;
    };
}
</script>
