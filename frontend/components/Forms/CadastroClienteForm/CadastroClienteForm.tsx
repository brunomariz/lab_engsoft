import { Form, Formik } from "formik";
import React from "react";
import {
  cadastroClienteValidation,
  ICadastroClienteValidation,
} from "../../../validation/cadastroCliente/cadastroClienteValidation";
import Input from "../../Input/Input";

type Props = {};

function CadastroClienteForm({}: Props) {
  const initialValues: ICadastroClienteValidation = {
    cpf_cliente: "",
    nome_cliente: "",
  };
  const handleSubmit = (values: ICadastroClienteValidation) => {
    console.log(values);
  };
  return (
    <div>
      <Formik
        initialValues={initialValues}
        onSubmit={(values, actions) => {
          handleSubmit(values);
          actions.setSubmitting(false);
        }}
        validationSchema={cadastroClienteValidation}
      >
        <Form>
          <div className="grid grid-cols-2">
            <Input label="CPF do Cliente" name="cpf_cliente"></Input>
            <Input label="Nome do Cliente" name="nome_cliente"></Input>
          </div>

          <button
            className="bg-slate-500 hover:bg-slate-700 text-white font-bold py-1 border-2 border-slate-500 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >
            Submit
          </button>
        </Form>
      </Formik>
    </div>
  );
}

export default CadastroClienteForm;
