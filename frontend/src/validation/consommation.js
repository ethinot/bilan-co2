import * as yup from "yup";

import { transportTypes, energyEmissionData } from "@/constants";

const energyTypes = Object.keys(energyEmissionData);

export const TripTracker = yup.object({
  type: yup
    .string()
    .oneOf(transportTypes, "Please select a valid transport type")
    .required("Please select a transpot type"),
  distance: yup
    .number("Please enter a the number")
    .min(0)
    .required("Please enter the distance"),
  date: yup.date("Please enter a date").required("The date is required"),
});

export const EnergyTracker = yup.object({
  type: yup
    .string()
    .oneOf(energyTypes, "Please select a valid transport type")
    .required("Please select a transpot type"),
  quantity: yup
    .number()
    .min(0, "Please enter a valid value")
    .required("The quantity is required"),
  date: yup.date("Please enter a date").required("The date is required"),
});
