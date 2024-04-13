<script setup>
import SideBar from "../components/dashboard/SideBar.vue";
</script>

<template>
  <div>
    <div class="fixed left-0 top-0 h-screen bg-[#03C988] w-[250px]">
      <SideBar class="h-full" />
    </div>
    <main class="ml-[250px]">
      <div class="p-1 border-b drop-shadow-lg">
        <ul class="flex items-center justify-end">
          User
        </ul>
      </div>
      <router-view class="p-4"></router-view>
    </main>
  </div>
</template>
