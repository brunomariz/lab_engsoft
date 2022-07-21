import React, { useState } from "react";
import { mockCostumers } from "../../constants/mock/mockCostumers";
import { mockEmployees } from "../../constants/mock/mockEmployees";
import { mockProducts } from "../../constants/mock/mockProdutos";
import { ICompraValidation } from "../../validation/compra/compraValidation";
import { IVendaValidation } from "../../validation/venda/vendaValidation";
import SidebarLayout from "../SidebarLayout/SidebarLayout";
import Table from "../Table/Table";

type Props = {
  values: ICompraValidation;
  handleConfirm: () => void;
  handleCancel: () => void;
};

const CompraConfirmation = ({ values, handleConfirm, handleCancel }: Props) => {
  let totalPrice = 0;
  return (
    <>
      <div className="flex space-x-3 mb-3">
        <div>
          <h3 className="my-2">Fornecedor</h3>
          <div className="">
            {
              mockCostumers.find(
                (costumer) =>
                  costumer.cpf_cliente.toString() ===
                  values.cnpj_fornecedor.toString()
              )?.nome
            }
          </div>
        </div>
        <div>
          <h3 className="my-2">Vendedor</h3>
          <div className="">
            {
              mockEmployees.find(
                (employee) =>
                  employee.cpf_funcionario.toString() ===
                  values.cpf_vendedor.toString()
              )?.nome_funcionario
            }
          </div>
        </div>
      </div>
      <Table
        columnTitles={["Codigo", "Nome", "Preço", "Quantidade", "Total"]}
        items={values.produtos.map((item) => {
          const product = mockProducts.find(
            (product) =>
              product.codigo_produto.toString() ===
              item.codigo_produto.toString()
          );
          const total = (product?.preco_venda || 0) * item.quantidade_produto;
          totalPrice += total;
          return {
            codigo: item.codigo_produto,
            nome: product?.nome_produto,
            preco: product?.preco_venda,
            quantidade: item.quantidade_produto,
            total: total,
          };
        })}
        title="Produtos"
      ></Table>
      <div
        className={`grid font-semibold text-slate-800 bg-gray-300 p-1 items-center`}
        style={{
          gridTemplateColumns: `repeat(${5}, 1fr)`,
        }}
      >
        <span>Soma dos produtos:</span>
        <span></span>
        <span></span>
        <span></span>
        <span className="">{totalPrice}</span>
      </div>
      <button
        onClick={handleCancel}
        className="mt-2 mr-2 bg-slate-500 hover:bg-orange-700 bg-opacity-25 text-white font-bold py-1 border-2 border-slate-500 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        Cancelar
      </button>
      <button
        onClick={handleConfirm}
        className="mt-2 bg-slate-500 hover:bg-slate-700 text-white font-bold py-1 border-2 border-slate-500 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        Confirmar
      </button>
    </>
  );
};

export default CompraConfirmation;
