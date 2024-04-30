import * as yup from "yup";

export const LoginSchema = yup.object({
  username: yup.string().required("The username is required"),
  password: yup.string().required("The password is required"),
});

export const SignupSchema = yup.object({
  username: yup.string().required("The username is required"),
  email: yup
    .string()
    .required("The email is required")
    .email("Enter a valid email"),
  password: yup
    .string()
    .min(6, "The password should contain at least 6 caracters")
    .required("The password is required"),
});
