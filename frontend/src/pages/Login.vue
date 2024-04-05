<script setup>
import LoginForm from "../components/auth/LoginForm.vue";
import Layout from "./Layout.vue";
</script>

<template>
  <Layout>
    <LoginForm/>
  </Layout>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
};
</script>
