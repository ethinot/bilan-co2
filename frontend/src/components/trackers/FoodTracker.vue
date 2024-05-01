<template>
  <div class="flex flex-col gap-4">
    <select
      v-model="selectedMainCategory"
      @change="updateSubcategories"
      class="px-4 py-2 rounded-md border border-gray-300 focus:outline-none focus:border-blue-500"
    >
      <option value="" disabled>Select Main Category</option>
      <option
        v-for="(subcategories, mainCategory) in categories"
        :value="mainCategory"
        :key="mainCategory"
      >
        {{ mainCategory }}
      </option>
    </select>
    <select
      v-model="selectedSubcategory"
      class="px-4 py-2 rounded-md border border-gray-300 focus:outline-none focus:border-blue-500"
    >
      <option value="" disabled>Select Subcategory</option>
      <option
        v-for="subcategory in filteredSubcategories"
        :value="subcategory"
        :key="subcategory"
      >
        {{ subcategory }}
      </option>
    </select>
  </div>
</template>

<script>
import { foodCategories } from "@/constants/index";

export default {
  data() {
    return {
      selectedMainCategory: "",
      selectedSubcategory: "",
      categories: foodCategories,
    };
  },
  computed: {
    filteredSubcategories() {
      return this.categories[this.selectedMainCategory] || [];
    },
  },
  methods: {
    updateSubcategories() {
      this.selectedSubcategory = "";
    },
  },
};
</script>
