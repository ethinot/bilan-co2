<script setup>
import NavBar from "../components/navbar/NavBar.vue";
import Footer from "../components/footer/Footer.vue";
</script>

<template>
  <div>
    <NavBar class="m-4" />
    <main class="my-8">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  components: {
    NavBar,
  },
};
</script>
