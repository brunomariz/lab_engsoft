import { Form, Formik } from "formik";
import { useRouter } from "next/router";
import React from "react";
import {
  cadastroClienteValidation,
  ICadastroClienteValidation,
} from "../../../validation/cadastroCliente/cadastroClienteValidation";
import {
  cadastroFornecedorValidation,
  ICadastroFornecedorValidation,
} from "../../../validation/cadastroFornecedor/cadastroFornecedorValidation";
import Input from "../../Input/Input";

type Props = {};

function CadastroFornecedorForm({}: Props) {
  const router = useRouter();
  const initialValues: ICadastroFornecedorValidation = {
    cnpj_fornecedor: "",
    nome_fornecedor: "",
  };
  const handleSubmit = (values: ICadastroFornecedorValidation) => {
    console.log(values);
    router.push("/home");
  };
  return (
    <div>
      <Formik
        initialValues={initialValues}
        onSubmit={(values, actions) => {
          handleSubmit(values);
          actions.setSubmitting(false);
        }}
        validationSchema={cadastroFornecedorValidation}
      >
        <Form>
          <div className="grid grid-cols-2">
            <Input label="CNPJ do Fornecedor" name="cnpj_fornecedor"></Input>
            <Input label="Nome do Fornecedor" name="nome_fornecedor"></Input>
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

export default CadastroFornecedorForm;
