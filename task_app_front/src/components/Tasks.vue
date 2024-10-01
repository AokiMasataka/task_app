<template>
    <div class="tasks">
            <v-card
                class="task"
                v-for="task in state.tasks"
                width="600px"
                :title="task.title"
                text="This is sample text"
                variant="tonal"
                @click="fetchTask(task.id)">
            </v-card>
        <AddTask></AddTask>
    </div>

    <v-dialog v-model="isActivate" max-width="600">
        <v-card title="Task Update Form">
            <v-card-text>
                <v-text-field
                    v-model="taskData.title"
                    label="Task Title*"
                    required>
                </v-text-field>
                <v-spacer></v-spacer>
                <v-textarea
                    v-model="taskData.content"
                    label="Content*"
                    rows="24"
                    required>
                </v-textarea>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn text="Close" variant="plain" @click="isActivate = false"></v-btn>
                <v-btn
                    color="#5865f2"
                    text="Save"
                    variant="tonal"
                    @click="updateTask"
                ></v-btn>
                <v-btn
                    color="red"
                    text="Delete"
                    variant="tonal"
                    @click="deleteTask"
                ></v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script setup lang="ts">
import {
deleteTaskAPI,
fetchTaskAPI,
fetchTasksAPI,
Task,
Tasks,
updateTaskAPI
} from '@/scripts/taskApi';
import { onMounted, reactive, ref } from 'vue';

let isActivate = ref(false);
const state = reactive<Tasks>({tasks: []});
const taskData = reactive<Task>({title: "", content: "", id: ""})

async function fetchTasks() {
    const tasks: Tasks = await fetchTasksAPI();
    state.tasks = tasks;
}

async function fetchTask(task_id: string) {
    const task = await fetchTaskAPI(task_id);
    taskData.title = task.title;
    taskData.content = task.content;
    taskData.id = task.id;
    isActivate.value = !isActivate.value;
}

const updateTask = async () => {
    const task_id = await updateTaskAPI(
        taskData.id,
        taskData.title,
        taskData.content
    );
    isActivate.value = false;
    location.reload();
    console.log(`task ID: ${task_id}`);
};

const deleteTask = async () => {
    deleteTaskAPI(taskData.id);
    location.reload();
}

onMounted(fetchTasks)
</script>

<style scoped>
.tasks {
    margin: 0px 64px 0px 64px;
}

.task {
    margin: 10px;
}
</style>