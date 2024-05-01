<script setup>
import CarIcon from "../../assets/car.png";
import FoodIcon from "../../assets/diet.png";
import ElectricityIcon from "../../assets/electrical.png";
import CategoryEmission from "@/components/dashboard/CategoryEmission.vue";
import CarbonDisplayer from "@/components/dashboard/CarbonDisplayer.vue";
import BarChart from "@/components/dashboard/BarChart.vue";
</script>

<template>
  <div class="p-2 overflow-y-scroll">
    <div class="flex h-fit items-center justify-center">
      <CarbonDisplayer :emission="emission" />
    </div>
    <div class="flex h-fit m-2 items-center justify-around gap-4">
      <CategoryEmission
        :percentage="tripsPercentage"
        label="Were emmited on trips"
        :categoryIcon="CarIcon"
      />

      <CategoryEmission
        :percentage="energyPercentage"
        label="Were emmited on electricity"
        :categoryIcon="ElectricityIcon"
      />
      <CategoryEmission
        :percentage="foodPercentage"
        label="Were emmited on food"
        :categoryIcon="FoodIcon"
      />
    </div>
    <div>
      <BarChart :data="[trips_emission, energy_emission, food_emission]" />
    </div>
  </div>
</template>

<script>
import { fetchConsommations } from "@/api/consommation";
export default {
  data() {
    return {
      emission: 0,
      food_emission: 0,
      energy_emission: 0,
      trips_emission: 0,
    };
  },

  computed: {
    foodPercentage() {
      return this.emission === 0
        ? 0
        : ((this.food_emission / this.emission) * 100).toFixed(2);
    },
    energyPercentage() {
      return this.emission === 0
        ? 0
        : ((this.energy_emission / this.emission) * 100).toFixed(2);
    },
    tripsPercentage() {
      return this.emission === 0
        ? 0
        : ((this.trips_emission / this.emission) * 100).toFixed(2);
    },
  },
  async mounted() {
    try {
      let sum = 0;
      const response = await fetchConsommations();
      const consommations = response.data;
      console.log(consommations);
      for (let index in consommations) {
        const consommation = consommations[index];
        console.log(consommation.type_consommation);
        if (consommation.type_consommation === "ALIMENTAIRE") {
          this.food_emission += consommations[index].quantite_co2;
        } else if (consommation.type_consommation === "TRANSPORT") {
          this.trips_emission += consommations[index].quantite_co2;
        } else {
          this.energy_emission += consommations[index].quantite_co2;
        }
        sum += consommations[index].quantite_co2;
      }
      this.emission = sum;
    } catch (error) {
      this.emission = 110;
    }
  },
};
</script>
