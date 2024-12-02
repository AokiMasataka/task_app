/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins';
import { createApp } from 'vue';
import App from './App.vue';
import './style.css';

const app = createApp(App)

registerPlugins(app)

app.mount('#app')
