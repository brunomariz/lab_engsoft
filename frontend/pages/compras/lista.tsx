import React from "react";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import Table from "../../components/Table/Table";
import { mockPurchases } from "../../constants/mock/mockPurchases";
import { mockSales } from "../../constants/mock/mockSales";

type Props = {};

function lista({}: Props) {
  return (
    <SidebarLayout title="Compras">
      <Table
        columnTitles={[
          "ID",
          "Data",
          "Valor Item",
          "Quantidade",
          "Código",
          "CPF Funcionario",
          "CNPJ Fornecedor",
        ]}
        items={mockPurchases}
        title="Lista de Compras"
      ></Table>
    </SidebarLayout>
  );
}

export default lista;
