import React from "react";
import SidebarLayout from "../components/SidebarLayout/SidebarLayout";
import Table from "../components/Table/Table";
import { mockEmployees } from "../constants/mock/mockEmployees";

type Props = {};

function Vendedores({}: Props) {
  return (
    <SidebarLayout title="Vendedores Ativos">
      <Table
        columnTitles={[
          "CPF",
          "Nome",
          "Salario Fixo",
          "Data de Admissao",
          "Cargo",
          "Comissão",
          "Usuario",
        ]}
        items={mockEmployees.map((item) => {
          return {
            ...item,
            eh_gerente: item.eh_gerente ? "Gerente" : "Funcionario",
          };
        })}
        title="Lista de Vendedores Ativos"
      ></Table>
    </SidebarLayout>
  );
}

export default Vendedores;
