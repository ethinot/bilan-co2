<template>
  <div
    class="flex items-center justify-center w-[150px] h-[150px] p-4 rounded-full border-[5px]"
    :class="borderColor"
  >
    <div class="text-center">
      <h2 class="font-semibold">CO2</h2>
      <p class="text-lg font-bold">{{ value }} kg</p>
      <p>So far this month</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: Number,
      required: true,
    },
  },
  computed: {
    borderColor() {
      if (this.value < 100) return "border-green-500";
      else if (this.value < 150) return "border-orange-500";
      else return "border-red-500";
    },
  },
};
</script>
