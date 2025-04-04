<template>
    <v-app-bar color="primary">
        <v-app-bar-title>
            <span class="cursor-pointer" @click="viewDoc">Task App</span>
        </v-app-bar-title>
    </v-app-bar>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
const router = useRouter();

function viewDoc() {
    router.push({ path: "/" });
}
</script>
