import { Form, Formik } from "formik";
import React, { useState } from "react";
import Select from "react-select";
import { mockProducts } from "../../../constants/mock/mockProdutos";
import {
  IVendaValidation,
  vendaValidation,
} from "../../../validation/venda/vendaValidation";
import Input from "../../Input/Input";

type Props = { setStep: Function; setValues: Function };

function VendaForm({ setStep, setValues }: Props) {
  const [numProducts, setnumProducts] = useState(1);
  const initialValues: IVendaValidation = {
    CPF_cliente: "",
    CPF_funcionario: "",
    produtos: [],
    // codigo_produto: 0,
    // em_promocao: false,
    // nome_produto: "",
    // preco_venda: 0,
    // quantidade_produto: 0,
  };
  const handleSubmit = (values: IVendaValidation) => {
    console.log(values);
    setValues(values);
    setStep(1);
  };
  return (
    <div>
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
            <Input label="CPF Funcionario" name="CPF_funcionario"></Input>
            <Input label="CPF Cliente" name="CPF_cliente"></Input>
          </div>
          {Array.apply(null, Array(numProducts)).map((item, index) => {
            return (
              <div className="grid grid-cols-12" key={index}>
                <div className="col-span-5">
                  <Input
                    label="Código do Produto"
                    name={`produtos.${index}.codigo_produto`}
                  ></Input>
                </div>
                <div className="col-span-5">
                  <Input
                    label="Quantidade de produtos"
                    name={`produtos.${index}.quantidade`}
                  ></Input>
                </div>
                <div className="col-span-2">
                  <Input label="Valor" name={`produtos.${index}.valor`}></Input>
                </div>
              </div>
            );
          })}
          <div
            onClick={() => setnumProducts(numProducts + 1)}
            className="hover:cursor-pointer inline-block text-slate-900 border-2 border-slate-900 font-bold py-1 mx-2 px-4 rounded focus:outline-none focus:shadow-outline"
          >
            + Produto
          </div>
          <button
            className="bg-slate-500 hover:bg-slate-700 text-white font-bold py-1 border-2 border-slate-500 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >
            Ir para confirmação
          </button>
        </Form>
      </Formik>
    </div>
  );
}

export default VendaForm;
