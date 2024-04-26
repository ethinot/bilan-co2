<template>
  <header class="flex items-center justify-between">
    <Logo />
    <Links />
  </header>
</template>

<script>
import Links from "./Links.vue";
import Logo from "./Logo.vue";

export default {
  components: {
    Logo,
    Links,
  },
};
</script>
