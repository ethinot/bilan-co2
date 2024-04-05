import { createMemoryHistory, createRouter } from 'vue-router'

import Login from "./src/pages/Login.vue";
import Home from "./src/pages/Home.vue";
import About from "./src/pages/About.vue";


const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path : '/about' , component : About}
]

export const router = createRouter({
  history: createMemoryHistory(),
  routes,
})