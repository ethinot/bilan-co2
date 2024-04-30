<script setup>
import Save from '@/components/save/Save.vue';
</script>

<template>
 
 <div class="relative ">
  <div class="absolute left-1/2 z-10 mt-5 flex w-screen max-w-max -translate-x-1/2 px-4">
    <div class="w-screen max-w-5xl flex-auto overflow-hidden rounded-3xl bg-white text-sm leading-6 shadow-lg ring-1 ring-gray-900/5">
      <div class="p-4 grid grid-cols-2 gap-5">
        <div class="group relative flex gap-x-6 rounded-lg p-4 max-w-3xl hover:bg-gray-100" v-for="(subCategories, category) in categories" :key="category"  >
          <div class="mt-1 flex h-11 w-11 flex-none items-center justify-center rounded-lg bg-gray-50 group-hover:bg-white">
          </div>
          <div class=" max-w-md " >
            <a href="#" class="flex font-semibold text-gray-900"> 
              <form class="max-w-sm mx-auto">
                <label for="countries" class="block mb-2 text-lg font-medium text-gray-900 dark:text-white">{{ category }}</label>
                <div>
                  <VueMultiselect
                  
                  v-model="multiValues[category]"
                  :options="subCategories"
                  :multiple="true" class=" text-md">
      
                  </VueMultiselect>
                </div>
              </form>
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
import VueMultiselect from 'vue-multiselect'
import { fetchTrackersAliment } from '@/api/trackers';


export default {
  data() {
    return {
      multiValues: {},
      categories: {}
    }
  },
  async mounted() {
    const reponse = await fetchTrackersAliment();
    this.categories= reponse;
  },
}

</script>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>