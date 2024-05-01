<template>
  <div
    class="flex items-center justify-center w-[150px] h-[150px] p-4 rounded-full border-[5px]"
    :class="borderColor"
  >
    <div class="text-center">
      <h2 class="font-semibold">CO2</h2>
      <p class="text-lg font-bold">{{ emissionValue }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ["emission"],
  computed: {
    borderColor() {
      if (this.kgValue < 100) return "border-green-500";
      else if (this.kgValue < 150) return "border-orange-500";
      else return "border-red-500";
    },
    emissionValue() {
      if (this.emission > 1000) {
        return `${(this.emission / 1000).toFixed(2)} Kg`;
      } else return `${this.emission} g`;
    },
    kgValue() {
      return this.emission / 1000;
    },
  },
};
</script>
