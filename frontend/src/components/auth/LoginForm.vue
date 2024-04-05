<script setup>
import CardWrapper from "../ui/CardWrapper.vue";
import { LoginSchema } from "../../validation/auth";
</script>

<template>
  <CardWrapper
    header-title="Welcome Back"
    back-button-label="Don't you have an account ?"
    back-button-url="/"
  >
    <Form
      action=""
      @submit.prevent="submitLogin"
      :validation-schema="LoginSchema"
    >
      <div class="w-full my-8">
        <label for="email" class="block">Email</label>
        <Field
          id="email"
          name="email"
          type="email"
          class="w-full rounded-sm p-2 outline-none focus-visible:border focus-visible:border-[#03C988]"
        />
        <ErrorMessage name="email" class="text-red-500" />

        {{}}
      </div>
      <div class="w-full my-8">
        <label for="password" class="block">Password</label>
        <Field
          id="password"
          name="password"
          type="password"
          class="w-full rounded-sm p-2 outline-none focus-visible:border focus-visible:border-[#03C988]"
        />
        <ErrorMessage name="password" class="text-red-500" />
      </div>
      <button
        class="w-full p-2 text-white font-semibold rounded-sm bg-[#03C988]"
      >
        Login
      </button>
    </Form>
  </CardWrapper>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    submitLogin() {
      console.log(this.email, this.password);
    },
  },
};
</script>
