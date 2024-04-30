<script setup>
import { Button } from "@/components/ui/button/index";
import LogoutIcon from "@/assets/logout.png";
</script>
<template>
  <button
    class="flex items-center justify-start gap-4 py-1 px-6 text-white font-semibold rounded-md hover:underline"
    @click="onLogoutClick"
  >
    <div class="w-[20px] h-[20px]">
      <img :src="LogoutIcon" />
    </div>
    <span>Logout</span>
  </button>
</template>

<script>
import { mapActions } from "vuex";
import { router } from "@/router";
export default {
  methods: {
    async onLogoutClick() {
      try {
        await this.logout();
        router.push({ name: "login" });
      } catch (error) {
        alert(error.message);
      }
    },
    ...mapActions(["logout"]),
  },
};
</script>
