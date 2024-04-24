<script setup>
import CarIcon from "../../assets/car.png";
import FoodIcon from "../../assets/diet.png";
import ElectricityIcon from "../../assets/electrical.png";
import OtherIcon from "../../assets/other.png";

import CategoryEmission from "@/components/dashboard/CategoryEmission.vue";

import CarbonDisplayer from "@/components/dashboard/CarbonDisplayer.vue";
</script>

<template>
  <div class="p-2">
    <div class="flex h-fit items-center justify-center">
      <CarbonDisplayer :value="120" />
    </div>
    <div class="flex h-fit m-2 items-center justify-around gap-4">
      <CategoryEmission
        :percentage="46"
        label="Were emmited on trips"
        :categoryIcon="CarIcon"
      />

      <CategoryEmission
        :percentage="30"
        label="Were emmited on electricity"
        :categoryIcon="ElectricityIcon"
      />
      <CategoryEmission
        :percentage="10"
        label="Were emmited on food"
        :categoryIcon="FoodIcon"
      />
      <CategoryEmission
        :percentage="14"
        label="Were emmited on other categories"
        :categoryIcon="OtherIcon"
      />
    </div>
  </div>
</template>
