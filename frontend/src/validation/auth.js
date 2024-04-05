import * as yup from "yup"

export const LoginSchema = yup.object({
    email : yup.string().required("The email is required").email("Enter a valid email"),
    password : yup.string().required("The password is required")
});