<script setup>
import LoginForm from "../../components/auth/LoginForm.vue";
</script>

<template>
  <LoginForm />
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
