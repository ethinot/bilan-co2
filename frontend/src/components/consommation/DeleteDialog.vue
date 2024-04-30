<template>
  <div v-if="show" class="fixed inset-0 flex items-center justify-center">
    <div
      class="absolute inset-0 bg-gray-900 bg-opacity-50"
      @click="cancel"
    ></div>
    <!-- Empty div for background opacity -->
    <div class="bg-white p-6 rounded-lg shadow-xl relative z-10">
      <!-- Confirmation dialog -->
      <div class="flex flex-col items-center">
        <h2 class="text-lg font-semibold mb-4">Confirm Delete</h2>
        <p class="text-sm text-gray-700 mb-4">
          Are you sure you want to delete this item?
        </p>
        <div class="flex justify-end">
          <button
            @click="cancel"
            class="mr-2 px-4 py-2 bg-gray-300 text-gray-800 rounded-lg hover:bg-gray-400"
          >
            Cancel
          </button>
          <button
            @click="confirm"
            class="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: {
      type: Boolean,
      required: true,
    },
    onConfirm: {
      type: Function,
      required: true,
    },
    onCancel: {
      type: Function,
      required: true,
    },
  },
  methods: {
    cancel() {
      this.onCancel();
    },
    confirm() {
      this.onConfirm();
    },
  },
};
</script>
