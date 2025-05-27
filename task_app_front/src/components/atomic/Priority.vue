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
                    <v-icon
                        :icon="IconCircle"
                        :color="colors[item.raw.value]"
                    />
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
// import { colors, prioritys } from "../const";
import IconCircle from "../icons/Circle.vue";

const prioritys = [
    { text: "low", value: 0 },
    { text: "midiam", value: 1 },
    { text: "high", value: 2 },
];

const colors = {
    0: "blue",
    1: "green",
    2: "red",
};

const priority = defineModel<number>("priority", { required: true });
</script>
