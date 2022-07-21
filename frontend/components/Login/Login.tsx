import React from "react";
import {
  Formik,
  FormikHelpers,
  FormikProps,
  Form,
  Field,
  FieldProps,
  useField,
  ErrorMessage,
} from "formik";
import { object, string, ref } from "yup";
import { loginValidation } from "../../validation/login/loginValidation";
import { useRouter } from "next/router";
import Input from "../Input/Input";

interface LoginFormValues {
  username: string;
  password: string;
}

type Props = {};

function Login({}: Props) {
  const initialValues: LoginFormValues = { username: "", password: "" };
  const router = useRouter();
  const handleSubmit = (values: LoginFormValues) => {
    console.log(values);
    if (true) {
      router.push("home");
    }
  };
  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <h1>Login</h1>
      <Formik
        initialValues={initialValues}
        onSubmit={(values, actions) => {
          handleSubmit(values);
          actions.setSubmitting(false);
        }}
        validationSchema={loginValidation}
      >
        <Form>
          <div className="flex flex-col items-center">
            <div>
              <Input label="Username" name="username"></Input>
              <Input label="Password" name="password" type="password"></Input>
            </div>
            <div className="flex items-center justify-between">
              <button
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                type="submit"
              >
                Submit
              </button>
            </div>
          </div>
        </Form>
      </Formik>
    </div>
  );
}

export default Login;
