import React from "react";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import Table from "../../components/Table/Table";
import { mockCostumers } from "../../constants/mock/mockCostumers";

type Props = {};

function ListaClientes({}: Props) {
  return (
    <SidebarLayout title="Clientes">
      <Table
        columnTitles={["Nome", "CPF"]}
        items={mockCostumers}
        title="Lista de Clientes"
      ></Table>
    </SidebarLayout>
  );
}

export default ListaClientes;
