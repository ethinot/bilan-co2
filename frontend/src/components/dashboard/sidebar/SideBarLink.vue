<template>
  <RouterLink
    class="flex items-center justify-start gap-4 py-1 px-6 text-white font-semibold rounded-md hover:underline"
    :to="to"
  >
    <div class="w-[20px] h-[20px]">
      <img :src="imageSource" />
    </div>
    <span>{{ label }}</span>
  </RouterLink>
</template>

<script>
export default {
  props: ["label", "imageSource", "to"],
};
</script>
