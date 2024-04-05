<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <nav class="">
    <!-- change them later to router links (when i'am done setting up the router) -->
    <ul class="flex items-center justify-end gap-10">
      <li class="font-semibold cursor-pointer">
        <RouterLink to="/">Home</RouterLink>
      </li>
      <li class="font-semibold cursor-pointer">
        <RouterLink to="/about">About</RouterLink>
      </li>
      <li class="font-semibold cursor-pointer">
        <RouterLink to="/login">Login</RouterLink>
      </li>
    </ul>
  </nav>
</template>

<style lang="scss" scoped></style>
