import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from "./stores/store.js";

// Import Bootstrap CSS and JS
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';
import './styles/global.css';

const app = createApp(App)
app.use(store)
app.use(router)
app.mount('#app');
