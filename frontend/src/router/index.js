import { createWebHistory, createRouter } from "vue-router";
import Layout from "../layouts/Layout.vue";
import DashboardLayout from "../layouts/DashboardLayout.vue";

import Home from "../pages/public/Home.vue";
import Login from "../pages/public/Login.vue";
import About from "../pages/public/About.vue";
import Register from "../pages/public/Register.vue";

import Dashboard from "../pages/protected/Dashboard.vue";
import TrackersEnergies from "@/pages/protected/TrackersEnergies.vue";
import TrackersTrips from "@/pages/protected/TrackersTrips.vue";
import TrackersAliments from "../pages/protected/TrackersAliments.vue";
import Consommations from "@/pages/protected/Consommations.vue";
import Settings from "@/pages/protected/Settings.vue";

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      component: Layout,
      children: [
        { path: "", component: Home, name: "home" },
        { path: "login", component: Login, name: "login" },
        { path: "register", component: Register, name: "register" },
        { path: "about", component: About, name: "about" },
      ],
    },
    {
      path: "/dashboard",
      component: DashboardLayout,
      children: [
        { path: "", component: Dashboard, name: "dashboard" },
        { path: "settings", component: Settings, name: "settings" },
        { path: "aliment", component: TrackersAliments, name: "aliment" },
        { path: "energies", component: TrackersEnergies, name: "energies" },
        { path: "trips", component: TrackersTrips, name: "trips" },
        {
          path: "consommations",
          component: Consommations,
          name: "consommations",
        },
      ],
    },
  ],
});
