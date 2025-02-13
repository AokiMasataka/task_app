<template>
    <v-card class="overflow-hidden">
        <v-card-title
            class="m-4 flex justify-between"
        >
            {{ formTitle }}
            <DeleteBtn v-if="props.isUpdateForm"
                @on-delete="$emit('onDelete')"
            />
            
        </v-card-title>
        
        <Selecters
            
            v-model:status="model.status"
            v-model:priority="model.priority"
            
            v-model:duedate="model.duedate"
            :is-update-form="props.isUpdateForm"
            
        />

        <v-card-text>
            <v-text-field
                v-model="model.title"
                variant="solo-filled"
                placeholder="input title"
                required
                :rules="[rules.required]"
            />
            <TextArea
                v-model:content="model.content"
                v-model:isPreviewMode="isPreviewMode"
            ></TextArea>
        </v-card-text>
        
        <v-divider />
        <v-card-actions class="px-6">
            <v-btn
                text="mode change"
                @click="isPreviewMode = !isPreviewMode"
            />
            <v-btn
                text="Close"
                variant="plain"
                @click="$emit('onClose')"
            />
            <v-btn
                :color="valid ? 'primary' : 'grey-darken-1'"
                text="Save"
                variant="tonal"
                @click="$emit('onSave')"
                :readonly="!valid"
            />
        </v-card-actions>
    </v-card>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue';
import { Task } from '../../scripts/types';
import DeleteBtn from '../DeleteBtn';
import Selecters from './Selecters.vue';
import TextArea from './TextArea.vue';


const props = defineProps<{isUpdateForm: boolean, isPreviewMode: boolean}>();
const model = defineModel<Task>({ required: true });
defineEmits<{
    (e: 'onClose'): void,
    (e: 'onSave'): void,
    (e: 'onDelete'): void,
}>();

const isPreviewMode = ref<boolean>(props.isPreviewMode);

const valid = computed(() => {
    return model.value.title != '';
})

const rules = {required: value => !!value || 'Field is required'}

const formTitle = computed(() => {
    return props.isUpdateForm ?  "Update Task" : "Create Task";
});

</script>
