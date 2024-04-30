import * as yup from "yup";

export const userDataSchema = yup.object({
  age: yup
    .number()
    .min(0, "Your age should be positif")
    .required("Please Enter your age"),
  profession: yup
    .string()
    .oneOf(["ET", "EMP", "CAD", "CHOM"])
    .required("Please select an option"),
  localisation: yup.string().required("Please enter your localisation"),
});
