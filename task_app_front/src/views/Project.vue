<template>
    <h1>{{ id }}</h1>

    <Sample>
        <div>
            <h1>Hello</h1>
        </div>
    </Sample>
</template>

<script setup lang="ts">
import { useRoute } from "vue-router";
import Sample from "../components/Sample.vue";

const route = useRoute();

const id = route.params.projectId;
</script>
