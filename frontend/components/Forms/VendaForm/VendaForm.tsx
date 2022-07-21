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
    cpf_cliente: "",
    cpf_vendedor: "",
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
  const codigoProdutoOptions = mockProducts.map((item) => item.codigo_produto);
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
            <Input label="CPF Vendedor" name="cpf_vendedor"></Input>
            <Input label="CPF Cliente" name="cpf_cliente"></Input>
          </div>
          {Array.apply(null, Array(numProducts)).map((item, index) => {
            return (
              <div className="grid grid-cols-12">
                <div className="col-span-6">
                  <Input
                    label="Código do Produto"
                    name={`produtos.${index}.codigo_produto`}
                  ></Input>
                  {/* <label
                    className="block text-gray-700 text-sm font-bold"
                    htmlFor={`produtos.${index}.codigo_produto`}
                  >
                    Código do Produto
                  </label> */}
                  {/* <select
                    className="p-3 rounded-lg "
                    name={`produtos.${index}.codigo_produto`}
                    id={`produtos.${index}.codigo_produto`}
                  >
                    {mockProducts.map((product) => {
                      return (
                        <option
                          value={product.codigo_produto}
                          label={product.codigo_produto}
                        ></option>
                      );
                    })}
                  </select> */}
                  {/* <Select options={codigoProdutoOptions}></Select> */}
                </div>
                <div className="col-span-6">
                  <Input
                    label="Quantidade de produtos"
                    name={`produtos.${index}.quantidade_produto`}
                  ></Input>
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
