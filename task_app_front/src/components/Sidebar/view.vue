<template>
    <div class="text-center">
        <v-navigation-drawer :width="240">
            <v-list-item
                class="mt-4"
                link
                title="Projects"
                @click="projects"
            ></v-list-item>
            <v-list-item
                class="mt-4"
                link
                title="setting"
                @click="setting"
            ></v-list-item>
        </v-navigation-drawer>
    </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();

function projects() {
    router.push({ path: "/projects" });
}

function setting() {
    alert("今後実装します");
}
</script>
