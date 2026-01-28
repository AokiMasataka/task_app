import { createApp } from 'vue';
import App from './App.vue';
import vuetify from "./plugins/vuetify.ts";
import router from './router.ts';
import './style.css';


const app = createApp(App);
app.use(vuetify);
app.use(router);
app.mount("#app");
