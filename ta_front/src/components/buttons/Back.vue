<template>
    <v-tooltip location="top">
        <template v-slot:activator="{ props }">
            <v-icon
                :icon="IconBack"
                v-bind="props"
                class="pt-1"
                @click.stop="$emit('onBack')"
            >
            </v-icon>
        </template>
        <span>back</span>
    </v-tooltip>
</template>

<script setup lang="ts">
import IconBack from "@/components/icons/Back.vue";

defineEmits<{ (e: "onBack"): void }>();
</script>
