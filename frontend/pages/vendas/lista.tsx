import React from "react";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import Table from "../../components/Table/Table";
import { mockSales } from "../../constants/mock/mockSales";

export interface IVendas {
  codigo_produto: number;
  CPF_cliente: string;
  quntidade_compra: number;
  data_compra: string;
  CPF_funcionario: string;
  valor_por_item: number;
}

type Props = {
  data: IVendas[];
};

function lista({ data }: Props) {
  return (
    <SidebarLayout title="Vendas">
      <Table
        columnTitles={[
          "Código",
          "CPF Cliente",
          "Quantidade",
          "Data",
          "CPF Funcionario",
          "Valor Item",
        ]}
        // items={mockSales}
        items={data}
        title="Lista de Vendas"
      ></Table>
    </SidebarLayout>
  );
}

// This gets called on every request
export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch(`http://localhost:8080/venda`);
  const data = await res.json();

  // Pass data to the page via props
  return { props: { data } };
}

export default lista;
