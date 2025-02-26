<template>
    <v-menu
        :close-on-content-click="false"
        location="end"
        v-model="viewCalendar"
    >
        <template v-slot:activator="{ props }">
            <v-text-field
                label="duedate"
                v-bind="props"
                v-model="displayDuedate"
                variant="underlined"
                hide-details="auto"
                readonly
                clearable
                :clear-icon="IconClose"
            >
            </v-text-field>
        </template>
        <v-date-picker
            v-model="duedate"
            color="primary"
            title="Set duedate"
        >
            <template v-slot:actions>
                <v-btn @click="viewCalendar = false">cancel</v-btn>
                <v-btn @click="saveDate">OK</v-btn>
            </template>
        </v-date-picker>
    </v-menu>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { dateToString } from '../../../scripts/date';
import IconClose from '../../icons/Close.vue';

const duedate = defineModel<Date | null>("duedate", { required: true });
const displayDuedate = ref<string | null>(null);
const viewCalendar = ref<boolean>(false);

function saveDate() {
    if (duedate.value != undefined){
        displayDuedate.value = dateToString(duedate.value);
    }

    viewCalendar.value = false;
}

onMounted(saveDate);
</script>