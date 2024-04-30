<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <nav class="">
    <ul class="flex items-center justify-end gap-10">
      <!-- <li class="font-semibold cursor-pointer">
        <RouterLink to="/">Home</RouterLink>
      </li>
      <li class="font-semibold cursor-pointer">
        <RouterLink to="/about">About</RouterLink>
      </li> -->
      <li class="font-semibold cursor-pointer">
        <RouterLink to="/login">Login</RouterLink>
      </li>
      <li class="font-semibold cursor-pointer">
        <RouterLink to="/register">Signup</RouterLink>
      </li>
    </ul>
  </nav>
</template>
