<template>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { BACKEND_BASE_URL } from '@/scripts/const';
import { callback } from '@/scripts/eaAuthClient';

const router = useRouter()

async function handleCallback() {
    try {
        const token = await callback(BACKEND_BASE_URL);
        // window.location.href = "/home";
        router.push("/projects");
    } catch (e) {
        alert("code verifier not found" + e);
        return;
    }
}

console.log("setup executed");
onMounted(async () => {
    await handleCallback();
});
//code verifier not foundTypeError: Cannot read properties of undefined (reading 'push')
</script>
