<script setup>
import { Table } from "@/components/ui/table";
</script>

<template>
  <div class="p-2">
    <div
      class="w-full h-full flex items-center justify-center"
      v-if="request.isSending"
    >
      <p class="font-semibold text-blue-500 text-xl">
        Fetching consommations data ...
      </p>
    </div>
    <div
      class="w-full h-full flex items-center justify-center"
      v-else-if="request.error"
    >
      <div class="flex flex-col justify-center gap-2">
        <p class="font-semibold text-red-500 text-xl">
          Something went wrong when fetching consommation data
        </p>
        <button
          class="w-fit m-auto p-2 bg-blue-500 text-white rounded-md self-center"
          @click="fethcData"
        >
          Press the button to refresh
        </button>
      </div>
    </div>
    <div
      class="w-full h-full flex items-center justify-center"
      v-else-if="consommations.length === 0"
    >
      <p class="font-semibold text-green-500 text-xl">
        You have no consommations
        {{ consommations.length }}
      </p>
    </div>
    <Table
      :consommations="consommations"
      :removeItem="removeConsommation"
      v-else
    />
  </div>
</template>

<script>
import { fetchConsommations } from "@/api/consommation";
export default {
  data() {
    return {
      consommations: [],
      request: {
        isSending: false,
        error: false,
      },
      fakeData: [
        {
          id: 1,
          type: "Aliment",
          emission: 2,
        },
        {
          id: 2,
          type: "Transport",
          emission: 50,
        },
        {
          id: 3,
          type: "Energie",
          emission: 70,
        },
      ],
    };
  },
  methods: {
    async fethcData() {
      try {
        this.request.isSending = true;
        this.request.error = false;
        // const response = await fetchConsommations();
        // this.consommations = response.data;
        this.consommations = this.fakeData;
        this.request.isSending = false;
      } catch (error) {
        this.request.isSending = false;
        this.request.error = true;
      }
    },
    removeConsommation(consommationId) {
      this.consommations = this.consommations.filter(
        (consommation) => consommation.id !== consommationId
      );
    },
  },
  provide() {
    return {
      removeItem: this.removeConsommation,
    };
  },
  async mounted() {
    try {
      await this.fethcData();
    } catch (error) {
      console.log("Somethin is going wrong");
    }
  },
};
</script>
