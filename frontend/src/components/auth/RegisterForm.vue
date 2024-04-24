<script setup>
import { SignupSchema } from "../../validation/auth";
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
      <CardTitle>Welcome Back !</CardTitle>
    </CardHeader>
    <CardContent>
      <Form
        action=""
        @submit.prevent="submitLogin"
        :validation-schema="SignupSchema"
      >
        <div class="w-full my-8">
          <label for="email" class="block">Full name</label>
          <Field
            id="fullName"
            name="fullName"
            type="text"
            class="w-full rounded-sm p-2 outline-none border focus-visible:border-[#03C988]"
          />
          <ErrorMessage name="fullName" class="text-red-500" />
        </div>
        <div class="w-full my-8">
          <label for="email" class="block">Email</label>
          <Field
            id="email"
            name="email"
            type="email"
            class="w-full rounded-sm p-2 outline-none border focus-visible:border-[#03C988]"
          />
          <ErrorMessage name="email" class="text-red-500" />
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
        <div class="w-full my-8">
          <label for="password" class="block">Confirm password</label>
          <Field
            id="confirmedPassword"
            name="confirmedPassword"
            type="password"
            class="w-full rounded-sm p-2 outline-none border focus-visible:border-[#03C988]"
          />
          <ErrorMessage name="confirmedPassword" class="text-red-500" />
        </div>
        <Button class="w-full font-semibold"> Register </Button>
      </Form>
    </CardContent>
    <CardFooter class="w-fit m-auto">
      <RouterLink class="underline" to="/login"
        >Already have an account ?</RouterLink
      >
    </CardFooter>
  </Card>
</template>

<script>
export default {
  data() {
    return {
      firstName: "",
      lastName: "",
      email: "",
      password: "",
      confirmedPassword: "",
    };
  },
  methods: {
    submitLogin() {
      console.log(this.email, this.password);
    },
  },
};
</script>
