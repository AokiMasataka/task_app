<template>
    <Navi></Navi>
    <div class="flex h-lvh w-11/12">
        <TaskList
            display-status="Todo"
            :value-status="state.Todo"
            :tasks="fetchedTasks.todo"
            @create-task="createTask"
            @update-task="updateTask"
            @delete-task="deleteTask"
        ></TaskList>
        <TaskList
            display-status="Doing"
            :value-status="state.Doing"
            :tasks="fetchedTasks.doing"
            @create-task="createTask"
            @update-task="updateTask"
            @delete-task="deleteTask"
        ></TaskList>
        <TaskList
            display-status="Done"
            :value-status="state.Done"
            :tasks="fetchedTasks.done"
            @create-task="createTask"
            @update-task="updateTask"
            @delete-task="deleteTask"
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
import Navi from '../templates/Navi.vue';


const fetchedTasks = ref<{
    todo: Tasks,
    doing: Tasks,
    done: Tasks
}>({todo: [], doing: [], done: []});

async function fetchTasks() {
    fetchedTasks.value.todo = await fetchTasksAPI(state.Todo);
    fetchedTasks.value.doing = await fetchTasksAPI(state.Doing);
    fetchedTasks.value.done = await fetchTasksAPI(state.Done);
}

async function createTask(task: Task): Promise<void> {
    await postTaskAPI(task.title, task.content, task.status);
    await fetchTasks();
};

async function updateTask(task: Task): Promise<void> {
    await updateTaskAPI(task.id, task.title, task.content, task.status);
    await fetchTasks();
}

async function deleteTask(task_id: string): Promise<void> {
    await deleteTaskAPI(task_id);
    await fetchTasks();
}

onMounted(fetchTasks);
</script>