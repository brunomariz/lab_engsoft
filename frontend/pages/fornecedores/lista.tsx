import React from "react";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import Table from "../../components/Table/Table";
import { mockCostumers } from "../../constants/mock/mockCostumers";
import { mockProviders } from "../../constants/mock/mockProviders";

type Props = {};

function ListaFornecedores({}: Props) {
  return (
    <SidebarLayout title="Fornecedores">
      <Table
        columnTitles={["Nome", "CNPJ"]}
        items={mockProviders}
        title="Lista de Fornecedores"
      ></Table>
    </SidebarLayout>
  );
}

export default ListaFornecedores;
