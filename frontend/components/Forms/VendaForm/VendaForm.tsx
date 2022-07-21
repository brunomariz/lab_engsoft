import { Form, Formik } from "formik";
import React from "react";
import {
  IVendaValidation,
  vendaValidation,
} from "../../../validation/venda/vendaValidation";
import Input from "../../Input/Input";

type Props = {};

function VendaForm({}: Props) {
  const initialValues: IVendaValidation = {
    cpf_cliente: "",
    cpf_vendedor: "",
    codigo_produto: 0,
    em_promocao: false,
    nome_produto: "",
    preco_venda: 0,
    quantidade_produto: 0,
  };
  const handleSubmit = (values: IVendaValidation) => {
    console.log(values);
  };
  return (
    <div>
      <h2 className="">Informações da Venda</h2>
      <Formik
        initialValues={initialValues}
        onSubmit={(values, actions) => {
          handleSubmit(values);
          actions.setSubmitting(false);
        }}
        validationSchema={vendaValidation}
      >
        <Form>
          <div className="grid grid-cols-2">
            <Input label="CPF Vendedor" name="cpf_vendedor"></Input>
            <Input label="CPF Cliente" name="cpf_cliente"></Input>
          </div>
          <div className="grid grid-cols-12">
            <div className="col-span-10">
              <Input label="Código do Produto" name="codigo_produto"></Input>
            </div>
            <div className="h-full flex items-center justify-center col-span-2">
              <input
                name="em_promocao"
                type="checkbox"
                className="scale-[2]"
              ></input>
              <label
                className="p-2 text-gray-700 text-sm font-bold"
                htmlFor="em_promocao"
              >
                Promoção
              </label>
            </div>
          </div>
          <div className="grid grid-cols-12">
            <div className="col-span-5">
              <Input label="Nome do Produto" name="nome_produto"></Input>
            </div>
            <div className="col-span-3">
              <Input
                label="Quantidade de produtos"
                name="quantidade_produto"
              ></Input>
            </div>
            <div className="col-span-4">
              <Input label="Preço da Venda" name="preco_venda"></Input>
            </div>
          </div>
          <button
            className="bg-slate-500 hover:bg-slate-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >
            Submit
          </button>
        </Form>
      </Formik>
    </div>
  );
}

export default VendaForm;
