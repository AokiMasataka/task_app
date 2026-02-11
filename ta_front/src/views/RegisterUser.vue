<template>
    <div class="register-user">
        <h1>Register User</h1>
        <form @submit.prevent="registerUser">
        <div>
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="name" required />
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="text" id="email" v-model="email" required />
        </div>
        <div>
            <label for="pass">Password:</label>
            <input type="text" id="pass" v-model="pass" required />
        </div>
        </form>
        <button @click="registerUser">Register</button>
    </div>
</template>
<script setup lang="ts">
import { ref } from 'vue'; 
import { createAccount } from '@/scripts/authApi';

const name = ref('');
const email = ref('');
const pass = ref('');

async function registerUser() {
    try {
        const response = await createAccount(name.value, email.value, pass.value);
        console.log('Account created successfully:', response);
    } catch (error) {
        console.error('Error creating account:', error);
    }
}

</script>