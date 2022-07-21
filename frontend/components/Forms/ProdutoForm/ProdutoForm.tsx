import { Form, Formik } from "formik";
import { useRouter } from "next/router";
import React from "react";
import { postData } from "../../../requests/postData";
import {
  cadastroClienteValidation,
  ICadastroClienteValidation,
} from "../../../validation/cadastroCliente/cadastroClienteValidation";
import {
  cadastroFornecedorValidation,
  ICadastroFornecedorValidation,
} from "../../../validation/cadastroFornecedor/cadastroFornecedorValidation";
import {
  IProdutoValidation,
  produtoValidation,
} from "../../../validation/produto/produtoValidation";
import Input from "../../Input/Input";

type Props = {};

function ProdutoForm({}: Props) {
  const router = useRouter();
  const initialValues: IProdutoValidation = {
    nome_produto: "",
    quantidade_produto: 0,
    em_promocao: false,
    preco_venda: 0,
  };
  const handleSubmit = (values: IProdutoValidation) => {
    console.log(values);
    postData(values, "/produto/create");
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
        validationSchema={produtoValidation}
      >
        <Form>
          <div className="grid grid-cols-2">
            <Input label="Nome do Produto" name="nome_produto"></Input>
            <Input
              label="Quantidade do Produto"
              name="quantidade_produto"
            ></Input>
            <Input
              label="Em Promoção"
              name="em_promocao"
              type="checkbox"
            ></Input>
            <Input label="Preço" name="preco_venda"></Input>
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

export default ProdutoForm;
