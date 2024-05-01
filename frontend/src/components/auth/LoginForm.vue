<script setup>
import { LoginSchema } from "../../validation/auth";
import { Form, Field, ErrorMessage } from "vee-validate";
import { Button } from "@/components/ui/button/index.js";
import {
  Card,
  CardHeader,
  CardTitle,
  CardFooter,
  CardContent,
} from "@/components/ui/card/index";
</script>

<template>
  <Card class="w-1/3 m-auto">
    <CardHeader class="text-center">
      <CardTitle>Welcome !</CardTitle>
    </CardHeader>
    <CardContent>
      <Form action="" @submit="submitLogin" :validation-schema="LoginSchema">
        <div class="w-full my-8">
          <label for="username" class="block">User name</label>
          <Field
            id="username"
            name="username"
            type="username"
            class="w-full rounded-sm p-2 outline-none border focus-visible:border-[#03C988]"
          />
          <ErrorMessage name="username" class="text-red-500" />

          {{}}
        </div>
        <div class="w-full my-8">
          <label for="password" class="block">Password</label>
          <Field
            id="password"
            name="password"
            type="password"
            class="w-full rounded-sm p-2 outline-none border focus-visible:border-[#03C988]"
          />
          <ErrorMessage name="password" class="text-red-500" />
        </div>
        <Button class="w-full font-semibold"> Login </Button>
      </Form>
    </CardContent>
    <CardFooter class="w-fit m-auto flex flex-col items-center">
      <p v-if="error" class="w-fit m-auto text-red-500 font-semibold">
        Invalid user name name or password
      </p>
      <p v-if="success" class="text-green-500 font-semibold">
        User Logged in successfully !
      </p>
      <RouterLink class="underline" to="/register"
        >Don't you have an account ?</RouterLink
      >
    </CardFooter>
  </Card>
</template>

<script>
import { mapActions } from "vuex";
import { router } from "@/router";

export default {
  data() {
    return {
      isSending: false,
      error: false,
      success: false,
    };
  },
  methods: {
    async submitLogin(values) {
      try {
        this.isSending = true;
        this.error = false;
        const response = await this.login(values);
        router.push({ name: "dashboard" });
      } catch (error) {
        console.log(error);
        this.error = true;
        this.isSending = false;
      }
    },
    ...mapActions(["login"]),
  },
};
</script>
