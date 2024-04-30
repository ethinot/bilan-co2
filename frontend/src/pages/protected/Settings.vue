<script setup>
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
  CardFooter,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Form, Field, ErrorMessage } from "vee-validate";
</script>

<template>
  <Card class="w-1/2 m-auto">
    <CardHeader class="flex items-center justify-center">
      <CardTitle>Edit you info here !</CardTitle>
    </CardHeader>
    <CardContent>
      <Form action="" @submit="submitEdit" :validation-schema="userDataSchema">
        <div class="w-full my-8">
          <label for="age" class="font-semibold block">Age</label>
          <Field
            id="age"
            name="age"
            type="number"
            ref="age"
            class="w-full rounded-sm p-2 outline-none border focus-visible:border-[#03C988]"
          />
          <ErrorMessage name="age" class="text-red-500" />

          {{}}
        </div>
        <div class="w-full my-8">
          <label for="profession" class="font-semibold block"
            >Select your status</label
          >
          <Field
            id="profession"
            name="profession"
            as="select"
            ref="select"
            className="w-full rounded-sm p-2 outline-none border focus-visible:border-[#03C988] appearance-none"
          >
            <option value="ET" className="text-green-600">Etudiant</option>
            <option value="EMP" className="text-blue-600">Employé</option>
            <option value="CAD" className="text-indigo-600">Cadre</option>
            <option value="CHOM" className="text-red-600">Chômeur</option>
          </Field>
          <ErrorMessage name="profession" class="text-red-500" />
        </div>
        <div class="w-full my-8">
          <label for="localisation" class="font-semibold block"
            >Localisation</label
          >
          <Field
            id="localisation"
            name="localisation"
            type="text"
            ref="localisation"
            v-model="user.localisation"
            class="w-full rounded-sm p-2 outline-none border focus-visible:border-[#03C988]"
          />
          <ErrorMessage name="localisation" class="text-red-500" />
        </div>
        <Button
          :disabled="request.isSending"
          class="w-full font-semibold bg-blue-500"
        >
          Edit
        </Button>
      </Form>
      <CardFooter>
        <p
          class="w-fit m-auto text-green-500 font-semibold"
          v-if="request.success"
        >
          Your data have been edited successfully
        </p>
        <p v-if="request.error" class="w-fit m-auto text-red-500 font-semibold">
          Something went wrong try again later !
        </p>
      </CardFooter>
    </CardContent>
  </Card>
</template>

<script>
import { fetchUserInfo, editUserInfo } from "@/api/user";
import { userDataSchema } from "@/validation/user";
export default {
  data() {
    return {
      user: {
        age: null,
        localisation: "",
        profession: "",
      },
      request: {
        isSending: false,
        error: false,
        success: false,
      },
    };
  },
  methods: {
    async submitEdit(values) {
      try {
        this.request.isSending = true;
        this.request.success = false;
        this.request.error = false;
        const response = await editUserInfo(values);
        if (response.status === 200 || response.status === 204) {
          this.request.isSending = false;
          this.request.success = true;
          setTimeout(() => {
            this.request.success = false;
          }, 5000);
        }
      } catch (error) {
        this.request.isSending = false;
        this.request.error = true;
        console.log(error);
      }
    },
    setUserData(user) {
      this.$refs.age.value = user.age;
      this.$refs.select.value = user.profession;
      this.$refs.localisation.value = user.localisation;
      console.log(this.user);
    },
    async fetchCurrentInfo() {
      try {
        const response = await fetchUserInfo();
        console.log(response);
        this.setUserData(response.data);
      } catch (error) {
        console.log(error);
      }
    },
  },
  async mounted() {
    try {
      await this.fetchCurrentInfo();
    } catch (error) {
      console.log(error);
    }
  },
};
</script>
