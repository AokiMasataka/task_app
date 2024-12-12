<template>
    <div class="flex justify-between h-lvh mx-8">
        <TaskList
            display-status="Todo"
            v-model:draggingTask="draggingTask"
            :value-status="state.Todo"
            :tasks="fetchedTasks.todo"
            :emphasislStatus="isEmphasislStatus(state.Todo)"
            @create-task="createTask"
            @update-task="updateTask"
            @delete-task="deleteTask"
            @on-drag-over="()=> emphasislStatus=state.Todo"
            @on-drop-task="updateTask"
            @on-drag-end="emphasislStatus=null"
        ></TaskList>
        <TaskList
            display-status="Doing"
            v-model:draggingTask="draggingTask"
            :value-status="state.Doing"
            :tasks="fetchedTasks.doing"
            :emphasislStatus="isEmphasislStatus(state.Doing)"
            @create-task="createTask"
            @update-task="updateTask"
            @delete-task="deleteTask"
            @on-drag-over="()=> emphasislStatus=state.Doing"
            @on-drop-task="updateTask"
            @on-drag-end="emphasislStatus=null"
        ></TaskList>
        <TaskList
            display-status="Done"
            v-model:draggingTask="draggingTask"
            :value-status="state.Done"
            :tasks="fetchedTasks.done"
            :emphasislStatus="isEmphasislStatus(state.Done)"
            @create-task="createTask"
            @update-task="updateTask"
            @delete-task="deleteTask"
            @on-drag-over="()=> emphasislStatus=state.Done"
            @on-drop-task="updateTask"
            @on-drag-end="emphasislStatus=null"
        ></TaskList>
    </div>
</template>

<script setup lang="ts">
import TaskList from '@/components/templates/Tasks.vue';
import { state } from '@/scripts/const';
import {
    deleteTaskAPI,
    fetchTasksAPI,
    postTaskAPI,
    updateTaskAPI
} from '@/scripts/taskApi';
import { Task, Tasks } from '@/scripts/types';
import { onMounted, ref } from 'vue';


const fetchedTasks = ref<{
    todo: Tasks,
    doing: Tasks,
    done: Tasks
}>({todo: [], doing: [], done: []});

const emphasislStatus = ref<number | null>(null);
const draggingTask = ref<Task | null>(null);

async function fetchTasks() {
    fetchedTasks.value.todo = await fetchTasksAPI(state.Todo);
    fetchedTasks.value.doing = await fetchTasksAPI(state.Doing);
    fetchedTasks.value.done = await fetchTasksAPI(state.Done);
};

async function createTask(task: Task): Promise<void> {
    await postTaskAPI(task.title, task.content, task.status);
    await fetchTasks();
};

async function updateTask(task: Task): Promise<void> {
    await updateTaskAPI(task.id, task.title, task.content, task.status);
    await fetchTasks();
    emphasislStatus.value = null
};

async function deleteTask(task_id: string): Promise<void> {
    await deleteTaskAPI(task_id);
    await fetchTasks();
};

function isEmphasislStatus(status: number): boolean {
    return emphasislStatus.value == status && draggingTask.value != null  && draggingTask.value.status != status
}

onMounted(fetchTasks);
</script>