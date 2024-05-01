<script setup>
import FoodTracker from "@/components/trackers/FoodTracker.vue";
import TripTracker from "@/components/trackers/TripTracker.vue";
import EnergyTracker from "@/components/trackers/EnergyTracker.vue";
import {
  Card,
  CardHeader,
  CardTitle,
  CardFooter,
  CardContent,
} from "@/components/ui/card/index";
</script>

<template>
  <div class="p-2">
    <Card class="w-4/5 m-auto">
      <CardHeader class="p-0 flex flex-row items-center justify-between">
        <CardTitle
          class="flex-1 p-2 border-b-[2px] border-gray-200 cursor-pointer"
          :class="{ 'border-b-green-500': activeTab === 'Food' }"
          @click="changeTab('Food')"
        >
          <h1 class="w-fit m-auto">Food Tracker</h1>
        </CardTitle>
        <CardTitle
          class="flex-1 p-2 border-b-[2px] border-gray-200 cursor-pointer"
          :class="{ 'border-b-green-500': activeTab === 'Trip' }"
          @click="changeTab('Trip')"
        >
          <h1 class="w-fit m-auto">Trip Tracker</h1>
        </CardTitle>
        <CardTitle
          class="flex-1 p-2 border-b-[2px] border-gray-200 cursor-pointer"
          :class="{ 'border-b-green-500': activeTab === 'Energy' }"
          @click="changeTab('Energy')"
        >
          <h1 class="w-fit m-auto">Energy Tracker</h1>
        </CardTitle>
      </CardHeader>
      <CardContent class="mt-4">
        <KeepAlive>
          <component :is="activeComponent" />
        </KeepAlive>
      </CardContent>
    </Card>
  </div>
</template>

<script>
export default {
  components: {
    FoodTracker,
    TripTracker,
    EnergyTracker,
  },
  data() {
    return {
      activeTab: "Food",
      activeComponent: FoodTracker,
    };
  },
  methods: {
    changeTab(tab) {
      if (tab === "Trip") {
        this.activeTab = "Trip";
        this.activeComponent = TripTracker;
      } else if (tab === "Energy") {
        this.activeTab = "Energy";
        this.activeComponent = EnergyTracker;
      } else {
        this.activeTab = "Food";
        this.activeComponent = FoodTracker;
      }
    },
  },
};
</script>
