import { object, string, ref } from "yup";

export const loginValidation = object().shape({
  username: string().required("Required"),
  password: string().min(8, "Required").required("Required"),
});
