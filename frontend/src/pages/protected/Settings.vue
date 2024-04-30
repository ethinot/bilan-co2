<template>
  <div>The settings page</div>
</template>

<script>
import { fetchUserInfo } from "@/api/user";
export default {
  async mounted() {
    console.log("the settings page is mounted !!");
    const response = await fetchUserInfo();
    console.log(response);
    try {
    } catch (error) {
      console.log(error);
    }
  },
};
</script>
