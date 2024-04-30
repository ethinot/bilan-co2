import { createApp } from 'vue'
import './style.css'
import App from './App.vue';
import { router } from './router/index'
import PrimeVue from 'primevue/config';

import store from './store';






const app =  createApp(App);


app.use(router);
app.use(PrimeVue ,{
    unstyled: true
});

app.use(store);

app.mount('#app')
