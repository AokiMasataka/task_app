<template>
    <div class="text-center">
        <v-navigation-drawer :width="240">
            <v-list-item link title="Projects" @click="projects"></v-list-item>
        </v-navigation-drawer>
    </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();

function projects() {
    router.push('/projects')
}

</script>
