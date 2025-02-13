<template>
    <v-app>
        <v-main>
            <Header></Header>
            <!-- <SideBer></SideBer> -->
            <TasksView></TasksView>
        </v-main>
    </v-app>
</template>

<script setup lang="ts">
import Header from './components/Header';
import TasksView from './views/TasksView';
</script>