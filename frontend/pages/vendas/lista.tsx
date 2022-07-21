import React from "react";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import Table from "../../components/Table/Table";
import { mockSales } from "../../constants/mock/mockSales";

type Props = {};

function lista({}: Props) {
  return (
    <SidebarLayout title="Vendas">
      <Table
        columnTitles={[
          "ID",
          "Data",
          "Valor Item",
          "Quantidade",
          "Código",
          "CPF Funcionario",
          "CPF Cliente",
        ]}
        items={mockSales}
        title="Lista de Vendas"
      ></Table>
    </SidebarLayout>
  );
}

export default lista;
