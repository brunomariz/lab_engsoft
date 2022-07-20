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

interface LoginFormValues {
  username: string;
  password: string;
}

type InputProps = { name: string; label: string; [x: string]: unknown };

const Input = ({ name, label, ...props }: InputProps) => {
  const [field, meta] = useField(name);
  return (
    <div className="mb-4">
      <label
        className="block text-gray-700 text-sm font-bold"
        htmlFor={field.name}
      >
        {label}
      </label>
      <input
        className={`${
          meta.error && meta.touched ? "border-red-500" : ""
        } shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline`}
        {...field}
        {...props}
      />
      <ErrorMessage
        name={field.name}
        component="div"
        className="text-red-500 text-xs"
      />
    </div>
  );
};

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
