<template>
    <v-menu>
        <template v-slot:activator="{ props }">
            <v-icon :icon="moreHori" v-bind="props" class="pt-1"></v-icon>
        </template>
        <v-list>
            <v-list-item
                v-for="(item, index) in props.items"
                :key="index"
                :value="index"
            >
                <template v-slot:prepend>
                    <v-icon :icon="item.icon"></v-icon>
                </template>
                <v-list-item-title @click="item.func()">{{
                    item.title
                }}</v-list-item-title>
            </v-list-item>
        </v-list>
    </v-menu>
</template>

<script setup lang="ts">
import moreHori from "@/components/icons/moreHori.vue";
import { Component } from "vue";
const props = defineProps<{
    items: { title: string; func: () => void; icon: Component }[];
}>();

function f() {
    alert("sample");
}
</script>
