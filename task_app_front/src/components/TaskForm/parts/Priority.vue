<template>
    <v-select
        v-model="priority"
        :items="prioritys"
        item-title="text"
        item-value="value"
        label="priority"
        variant="underlined"
        hide-details="auto"
    >
        <template v-slot:item="{ props, item }">
            <v-list-item v-bind="props" :title="item.raw.text" slim>
                <template v-slot:prepend>
                    <v-icon :icon="IconCircle" :color="colors[item.raw.value]"/>
                </template>
            </v-list-item>
        </template>

        <template v-slot:selection="{ item, index }">
            <v-chip :color="colors[item.raw.value]" variant="flat">
                {{ item.raw.text }}
            </v-chip>
        </template>
    </v-select>
</template>

<script setup lang="ts">
import IconCircle from '../../icons/Circle.vue';
import { colors, prioritys } from '../const';

const priority = defineModel<number>("priority", { required: true });
</script>