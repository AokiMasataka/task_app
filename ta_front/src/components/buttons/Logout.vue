<template>
    <v-btn @click="handleLogout">Logout</v-btn>
</template>
<script setup lang="ts">
import { useRouter } from 'vue-router';
import { logoutApi } from '@/scripts/eaAuthClient';
import { BACKEND_BASE_URL } from '@/scripts/const';

async function handleLogout() {
    try {
        await logoutApi(BACKEND_BASE_URL);
        const router = useRouter();
        router.push("/");
    } catch (e) {
        alert("Error during logout: " + e);
    }
}

</script>