<script setup>
import SideBarLink from "./SideBarLink.vue";
import HomeIcon from "@/assets/home.png";
import SettingsIcon from "@/assets/settings.png";
import TrackIcon from "@/assets/track.png";
import LogoutIcon from "@/assets/logout.png";
</script>
<template>
  <nav class="p-2">
    <div class="flex items-center justify-center">
      <h1 class="font-semibold text-3xl text-white m-auto">Carbon Tracker</h1>
    </div>
    <ul class="h-full p-4 flex flex-col justify-around">
      <div class="flex flex-col gap-8" >
        <li class="">
          <SideBarLink
            label="Dashboard"
            to="/dashboard"
            :imageSource="HomeIcon"
          />
        </li>
        <li class=""  >
          <SideBarLink 
            @click="toogglevisibility"
           
            label="Add tracker"
            to=""
            :imageSource="TrackIcon"
          />
          <div v-if="isVisible"  class=" absolute mt-2 w-48 z-20  rounded-md shadow-xl bg-white "  v-click-outside="onClickOutside">
   <router-link to="/dashboard/aliment" 
   class="
     block
     px-4
     py-2
     text-sm
     capitalize
     text-gray-700
     hover:bg-gray-300
     hover:text-white
   "
   > Aliments    
   </router-link>
   <router-link to="/dashboard/trips" 
   class="
     block
     px-4
     py-2
     text-sm
     capitalize
     text-gray-700
     hover:bg-gray-300
     hover:text-white
   "
   > Trajet   
   </router-link>
   <router-link to="/dashboard/energies" 
   class="
     block
     px-4
     py-2
     text-sm
     capitalize
     text-gray-700
     hover:bg-gray-300
     hover:text-white
   "
   > Energies   
   </router-link>
  </div>
        </li>
        <li class="">
          <SideBarLink
            label="Settings"
            to="/dashboard"
            :imageSource="SettingsIcon"
          />
        </li>
      </div>
      <div class="">
        <SideBarLink label="Logout" to="/dashboard" :imageSource="LogoutIcon" />
      </div>
    </ul>
  </nav>
</template>
<script>
import vClickOutside from "v-click-outside";
export default {
  directives: {
    clickOutside: vClickOutside.directive
  },
  data() {
    return {
      isVisible:false,
    }
  },
  methods: {
    toogglevisibility(){
      this.isVisible=!this.isVisible;
    },
    onClickOutside(){
      if (this.isVisible) {
        this.isVisible=false;
        
      }
    }
  }
}
</script>
