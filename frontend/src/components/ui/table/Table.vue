<script setup>
import TableItem from "./TableItem.vue";
</script>

<template>
  <div class="overflow-x-auto">
    <table class="w-full whitespace-no-wrap bg-white divide-y divide-gray-200">
      <thead class="bg-gray-200">
        <tr>
          <th
            class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider"
          >
            ID
          </th>
          <th
            class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider"
          >
            Consommation Name
          </th>
          <th
            class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider"
          >
            Consommation type
          </th>
          <th
            class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider"
          >
            CO2 Amount
          </th>
          <th class="px-6 py-3"></th>
        </tr>
      </thead>
      <tbody class="divide-y divide-gray-200">
        <TableItem
          v-for="consommation in consommations"
          :id="consommation.id"
          :type="consommation.type"
          :emission="consommation.emission"
        />
      </tbody>
    </table>
  </div>
</template>

<script>
import { deleteConsommation } from "@/api/consommation";
export default {
  data() {
    return {
      request: {
        isSending: false,
        error: false,
      },
    };
  },
  props: {
    consommations: {
      type: Array,
      required: true,
    },
  },
};
</script>
