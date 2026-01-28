<template>
    <v-app>
        <v-main>
            <Header></Header>
            <Sidebar></Sidebar>
            <router-view/>
        </v-main>
    </v-app>
</template>

<script setup lang="ts">
import Header from './components/Header';
import Sidebar from './components/Sidebar';
</script>