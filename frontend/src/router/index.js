import { createWebHistory, createRouter } from 'vue-router'

import Layout from "../layouts/Layout.vue";
import DashboardLayout from "../layouts/DashboardLayout.vue";




import Home from "../pages/public/Home.vue";
import Login from "../pages/public/Login.vue";
import About from "../pages/public/About.vue";
import Register from '../pages/public/Register.vue';


import Dashboard from "../pages/protected/Dashboard.vue";
import Trackers from '@/pages/protected/Trackers.vue';


export const router = createRouter({
  history: createWebHistory(),
  routes : [
    {
      path : '/',
      component : Layout,
      children : [
        {path : '' , component  : Home , name : 'home'},
        {path : 'login' , component : Login , name: 'login' },
        {path : 'register' , component : Register , name : 'register'},
        {path : 'about' , component : About , name : 'about' }
      ]
    },
    {
      path : '/dashboard',
      component : DashboardLayout,
      children : [
        {path : '' , component : Dashboard , name : 'dashboard'},
        {path : 'trackers' , component : Trackers , name : 'trackers'}
      ]
    }
  ]
})