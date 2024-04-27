import { createStore } from "vuex";

import { login } from "@/api/auth";


const store = new createStore({
    state: {
      auth_token: localStorage.getItem('auth_token') || null,
      isAuthenticated: localStorage.getItem('auth_token') ? true : false
    },
    mutations: {
      setToken(state, token) {
        state.auth_token = token;
        localStorage.setItem('auth_token', token);
        state.isAuthenticated = true;
      },
      removeToken(state) {
        state.auth_token = null;
        localStorage.removeItem('auth_token');
        state.isAuthenticated = false;
      }
    },
    actions: {
      async login({ commit }, credentials) {
        try {
          
          const response = await login(credentials);
          const token = response.data.auth_token;
          if (response.status === 200) {
            commit('setToken', token);
          } else {
            throw new Error("Something went wrong !")
          }
          
        } catch (error) {
            throw error;
        }
      },
      logout({ commit }) {
        commit('removeToken');
      }
    },
    getters: {
      isAuthenticated: state => state.isAuthenticated
    }
  });

export default store;
