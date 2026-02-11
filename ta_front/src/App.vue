<template>
    <v-app>
        <v-main>
            <router-view/>
        </v-main>
    </v-app>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { refreshApi } from './scripts/eaAuthClient';
import { BACKEND_BASE_URL } from './scripts/const';
import { me } from '@/scripts/authApi';


const router = useRouter();

async function refresh() {
    try {
        const token = await refreshApi(BACKEND_BASE_URL);
        const user = await me(token);
    } catch (e) {
        console.log("No valid refresh token found: " + e);
        router.push("/");
    }
    
}

onMounted(async () => {
    await refresh();
});

</script>