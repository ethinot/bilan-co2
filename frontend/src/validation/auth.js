import * as yup from "yup"

export const LoginSchema = yup.object({
    email : yup.string().required("The email is required").email("Enter a valid email"),
    password : yup.string().required("The password is required")
});

export const SignupSchema = yup.object({
    fullName : yup.string().required('The full name is required'),
    email : yup.string().required("The email is required").email("Enter a valid email"),
    password : yup.string().min(6 , "The password should contain at least 6 caracters").required("The password is required"),
    confirmedPassword : yup.string().required("The password confirmation is required")
})