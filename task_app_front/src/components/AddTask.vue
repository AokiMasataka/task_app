<template>

    <div class="btn">
        <button @click="isActivate = !isActivate">
            <v-card
                class="text-center"
                width="600px"
                title="+"
            >
            </v-card>
        </button>
    </div>

    <v-dialog v-model="isActivate" max-width="600">
        <v-card title="Create Task Form">
            <v-card-text>
                <v-text-field
                    v-model="taskData.title"
                    label="Task Title*"
                    required>
                </v-text-field>
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
                    @click="submit"
                ></v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script setup lang="ts">
import { postTaskAPI } from '@/scripts/taskApi';
import { reactive, ref } from 'vue';

let isActivate = ref(false);
const taskData = reactive({title: "", content: ""});

const submit = async () => {
    const task_id = await postTaskAPI(taskData.title, taskData.content);
    isActivate.value = false;
    location.reload();
    console.log(`task ID: ${task_id}`);
};

</script>

<style scoped>
.btn{
    margin: 10px;
}
</style>