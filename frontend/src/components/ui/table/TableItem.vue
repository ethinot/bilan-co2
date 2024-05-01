<script setup>
import DeleteDialog from "@/components/consommation/DeleteDialog.vue";
</script>
<template>
  <tr class="hover:bg-gray-100">
    <td class="px-6 py-4 whitespace-nowrap">{{ id }}</td>
    <td class="px-6 py-4 whitespace-nowrap">{{ name }}</td>
    <td class="px-6 py-4 whitespace-nowrap">{{ type }}</td>
    <td class="px-6 py-4 whitespace-nowrap">{{ emmisionValue }}</td>
    <td class="px-6 py-4 whitespace-nowrap">
      <button
        class="text-red-600 hover:text-red-800 font-bold"
        :onclick="
          () => {
            show = true;
          }
        "
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          class="w-4 h-4 inline-block align-middle"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>
    </td>
  </tr>
  <DeleteDialog
    :show="show"
    :onConfirm="onDelete"
    :onCancel="
      () => {
        show = false;
      }
    "
  />
</template>

<script>
import { deleteConsommation } from "@/api/consommation";
export default {
  data() {
    return {
      show: false,
      request: {
        isSending: false,
        error: false,
      },
    };
  },
  methods: {
    async onDelete() {
      try {
        this.request.isSending = true;
        this.request.error = false;
        const response = await deleteConsommation(this.id);
        this.removeItem(this.id);
        this.show = false;
      } catch (error) {
        this.request.error = true;
        this.request.isSending = false;
        console.log(error);
        console.log("Someting went wrong when deleting the consommation");
      }
    },
  },
  props: ["id", "name", "type", "emission"],
  inject: ["removeItem"],
  computed: {
    emmisionValue() {
      if (this.emission > 1000) {
        return `${(this.emission / 1000).toFixed(2)} Kg`;
      } else return `${this.emission} g`;
    },
  },
};
</script>
