<template>
  <div class="border w-1/3 m-auto rounded-md drop-shadow p-4">
    <header class="m-4">
      <h2 class="text-xl font-semibold w-fit m-auto">{{ headerTitle }}</h2>
    </header>
    <main class="m-4"><slot></slot></main>
    <footer class="flex items-center justify-center m-4">
      <a :href="backButtonUrl" class="underline">{{ backButtonLabel }}</a>
    </footer>
  </div>
</template>

<script>
export default {
  props: ["headerTitle", "backButtonLabel", "backButtonUrl"],
};
</script>
