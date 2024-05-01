<script setup>
import { Form, Field, ErrorMessage } from "vee-validate";
import { TripTracker } from "@/validation/consommation";
import { Button } from "../ui/button";
</script>
<template>
  <div class="flex flex-col gap-4">
    <Form :validation-schema="TripTracker" @submit="submitCalculate">
      <div class="w-full my-8">
        <label for="profession" class="font-semibold block"
          >Select the transport type</label
        >
        <Field
          id="type"
          name="type"
          as="select"
          ref="transport"
          className="w-full rounded-sm p-2 outline-none border focus-visible:border-[#03C988] appearance-none"
        >
          <option value="" disabled>Select Transport type</option>
          <option
            v-for="transport in transportOptions"
            :value="transport"
            :key="transport"
          >
            {{ transport }}
          </option>
        </Field>
        <ErrorMessage name="type" class="text-red-500" />
      </div>
      <div class="w-full my-8">
        <label for="age" class="font-semibold block">Distance (in KM)</label>
        <Field
          id="distance"
          name="distance"
          type="number"
          ref="distance"
          class="w-full rounded-sm p-2 outline-none border focus-visible:border-[#03C988]"
        />
        <ErrorMessage name="distance" class="text-red-500" />

        {{}}
      </div>
      <div class="w-full my-8">
        <label for="date" class="font-semibold block">Date</label>
        <Field
          id="date"
          name="date"
          type="date"
          ref="date"
          class="w-full rounded-sm p-2 outline-none border focus-visible:border-[#03C988]"
        />
        <ErrorMessage name="date" class="text-red-500" />

        {{}}
      </div>
      <div v-if="emission">
        <div class="font-semibold">
          <span
            >Emission : <span class="tetx-red-500">{{ emission }} g</span></span
          >
        </div>

        <Button
          :disabled="save.isSending"
          type="button"
          @click="submitSave"
          class="w-full font-semibold bg-green-500"
        >
          Save emission
        </Button>
      </div>
      <Button
        :disabled="calculate.isSending"
        v-show="!calculate.success"
        class="w-full font-semibold bg-blue-500"
      >
        Calculate
      </Button>
    </Form>
  </div>
</template>

<script>
import { transportEmissionData } from "@/constants/index";
import { createConsommation } from "@/api/consommation";
import { router } from "@/router";
export default {
  data() {
    return {
      transportEmissionData: transportEmissionData,
      emission: null,
      reason: "",
      calculate: {
        isSending: false,
        error: false,
        success: false,
      },
      save: {
        isSending: false,
        error: false,
      },
    };
  },
  methods: {
    async submitCalculate(values) {
      await this.calucateEmission(values.type, values.distance);
    },
    async calucateEmission(type, quantity) {
      try {
        this.calculate.isSending = true;
        this.calculate.error = false;
        // const response = await calculateTripConsommation({ type, quantity });
        setTimeout(() => {
          this.emission = transportEmissionData[type] * quantity;
          console.log(this.emission);
          this.calculate.isSending = false;
          this.calculate.success = true;
        }, 2000);
      } catch (error) {
        this.calculate.isSending = false;
        this.calculate.error = false;
        console.log("Error");
        alert("Something went wrong try again later");
      }
    },
    async saveEmission() {
      try {
        this.save.isSending = true;
        this.save.error = false;
        const response = await createConsommation({
          type: "TRANSPORT",
          reason: this.$refs.transport.value,
          quantity: this.emission,
          date: this.$refs.date.value,
        });
        this.save.isSending = false;
      } catch (error) {
        this.save.error = true;
        this.save.isSending = false;
        alert("Something went wrong when trying to save data");
        return;
      }
    },
    async submitSave() {
      await this.saveEmission();
      router.push({ name: "consommations" });
    },
  },
  computed: {
    transportOptions() {
      // Get the keys of the transportEmissionData object
      return Object.keys(this.transportEmissionData);
    },
  },
};
</script>
