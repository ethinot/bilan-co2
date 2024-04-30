import { createStore } from "vuex";

import { login, logout } from "@/api/auth";

const store = new createStore({
  state: {
    auth_token: localStorage.getItem("auth_token") || null,
    isAuthenticated: localStorage.getItem("auth_token") ? true : false,
  },
  mutations: {
    setToken(state, token) {
      state.auth_token = token;
      localStorage.setItem("auth_token", token);
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.auth_token = null;
      localStorage.removeItem("auth_token");
      state.isAuthenticated = false;
    },
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await login(credentials);
        const token = response.data.auth_token;
        if (response.status === 200) {
          commit("setToken", token);
        } else {
          throw new Error("Something went wrong when trying to log you in !");
        }
      } catch (error) {
        throw error;
      }
    },
    async logout({ commit }) {
      try {
        // Temporary fix for logout problem :
        commit("removeToken");
        return;
        const response = await logout();
        if (response.status === 200) {
          commit("removeToken");
        } else {
          throw new Error("Something went wrong when trying to log you out !");
        }
      } catch (error) {
        throw error;
      }
    },
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    auth_token: (state) => state.auth_token,
  },
});

export default store;
