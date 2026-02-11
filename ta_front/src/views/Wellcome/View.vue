<template>
  <div class="welcome">
    <h1 class="app-title">My Awesome App</h1>

    <button class="login-button" @click="goToLogin">
      ログインへ
    </button>
    <button class="login-button" @click="createAccount">
        Create Account
    </button>
  </div>
</template>

<script setup>
import { redirectLoginForm } from '@/scripts/eaAuthClient';
import { useRouter } from 'vue-router';

async function goToLogin() {
    const eaLoginFormUrl = "http://localhost/login";
    const client_id = "1234";
    await redirectLoginForm(eaLoginFormUrl, client_id);
}

async function createAccount() {
    useRouter().push("/register");
}
</script>

<style scoped>
.welcome {
  min-height: 100vh;
  background: #202123;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.app-title {
  color: #ffffff;
  font-size: 2.5rem;
  margin-bottom: 2rem;
  letter-spacing: 0.05em;
}

.login-button {
  background: #8934ba;
  color: #ffffff;
  border: none;
  padding: 0.8rem 2.5rem;
  font-size: 1.1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: opacity 0.2s, transform 0.2s;
}

.login-button:hover {
  opacity: 0.9;
  transform: translateY(-2px);
}
</style>