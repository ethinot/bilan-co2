<script setup>
import Save from '@/components/save/Save.vue';
</script>

<template>
 
 <div class="relative ">
  <div class="absolute left-1/2 z-10 mt-5 flex w-screen max-w-max -translate-x-1/2 px-4">
    <div class="w-screen max-w-5xl flex-auto overflow-hidden rounded-3xl bg-white text-sm leading-6 shadow-lg ring-1 ring-gray-900/5">
      <div class="p-4 grid grid-cols-2">
        <div class="group relative flex gap-x-6 rounded-lg p-4 hover:bg-gray-100" v-for="energieid in energies" :key="energieid"  >
          <div class="mt-1 flex h-11 w-11 flex-none items-center justify-center rounded-lg bg-gray-50 group-hover:bg-white">
          </div>
          <div >
            <a href="#" class="font-semibold text-gray-900">
              {{ energieid }}
              <span class="absolute inset-0"></span>
            </a>
            <p class="mt-1 text-gray-600"></p><b/>
          </div>
        </div>
      </div>
      <Save/>
    </div>
  </div>
</div>


</template>
<script>
import { fetchTrackersEnergie } from '@/api/trackers';
export default {
  data() {
    return {
      energies: null
    }
  },
  async mounted() {
    const reponse = await fetchTrackersEnergie();
    this.energies= reponse;
  },
}

</script>