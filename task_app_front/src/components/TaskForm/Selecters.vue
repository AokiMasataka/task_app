<template>
    <v-row class="mx-4">
        <v-col v-if="props.isUpdateForm" cols="12" sm="6" md="3">
            <v-select
                v-model="status"
                :items="items"
                item-title="text"
                item-value="value"
                label="status"
                variant="underlined"
            />
        </v-col>

        <v-col cols="12" sm="6" md="3">
            <v-select
                v-model="priority"
                :items="prioritys"
                item-title="text"
                item-value="value"
                label="priority"
                variant="underlined"
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
        </v-col>
        
        <v-col cols="12" sm="6" md="3">
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
        </v-col>
    
    </v-row>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { dateToString } from '../../scripts/date';
import IconCircle from '../icons/Circle.vue';
import IconClose from '../icons/Close.vue';
import { colors, items, prioritys } from './const';

const props = defineProps<{isUpdateForm: boolean}>();
const status = defineModel<number>("status", { required: true });
const priority = defineModel<number>("priority", { required: true });
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