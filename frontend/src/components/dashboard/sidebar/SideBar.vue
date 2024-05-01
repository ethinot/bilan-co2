<script setup>
import SideBarLink from "./SideBarLink.vue";
import HomeIcon from "@/assets/home.png";
import SettingsIcon from "@/assets/settings.png";
import TrackIcon from "@/assets/track.png";
import CarbonIcon from "@/assets/carbon.png";
import LogoutButton from "./LogoutButton.vue";
</script>
<template>
  <nav class="p-2">
    <div class="flex items-center justify-center">
      <h1 class="font-semibold text-3xl text-white m-auto">Carbon Tracker</h1>
    </div>
    <ul class="h-full p-4 flex flex-col justify-around">
      <div class="flex flex-col gap-8">
        <li class="">
          <SideBarLink
            label="Dashboard"
            to="/dashboard"
            :imageSource="HomeIcon"
          />
        </li>
        <li class="">
          <SideBarLink
            label="Add Tracker"
            to="/dashboard/trackers"
            :imageSource="TrackIcon"
          />
        </li>
        <li class="">
          <SideBarLink
            label="Consommations"
            to="/dashboard/consommations"
            :imageSource="CarbonIcon"
          />
        </li>
        <li class="">
          <SideBarLink
            label="Settings"
            to="/dashboard/settings"
            :imageSource="SettingsIcon"
          />
        </li>
      </div>
      <div>
        <LogoutButton />
      </div>
    </ul>
  </nav>
</template>
<script>
import vClickOutside from "v-click-outside";
export default {
  directives: {
    clickOutside: vClickOutside.directive,
  },
  data() {
    return {
      isVisible: false,
    };
  },
  methods: {
    toogglevisibility() {
      this.isVisible = !this.isVisible;
    },
    onClickOutside() {
      if (this.isVisible) {
        this.isVisible = false;
      }
    },
  },
};
</script>
