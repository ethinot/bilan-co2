<script setup>
import {
  Card,
  CardTitle,
  CardHeader,
  CardContent,
  CardDescription,
} from "@/components/ui/card/index";
</script>

<template>
  <Card class="flex flex-row-reverse items-center py-4 px-2 w-[200px]">
    <div class="text-center">
      <CardHeader class="p-0">
        <CardTitle class="text-3xl">{{ percentage }}%</CardTitle>
      </CardHeader>
      <CardDescription>
        <p>{{ label }}</p>
      </CardDescription>
    </div>

    <CardContent class="p-0">
      <div
        class="flex items-center justify-center bg-blue-300 p-2 rounded-full"
      >
        <img :src="categoryIcon" width="70" height="70" />
      </div>
    </CardContent>
  </Card>
</template>

<script>
export default {
  props: ["percentage", "categoryIcon", "label"],
};
</script>
