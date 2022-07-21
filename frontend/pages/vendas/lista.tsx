import React from "react";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import Table from "../../components/Table/Table";
import { mockSales } from "../../constants/mock/mockSales";

interface IVendas {
  id_venda: number;
  data_venda: string;
  valor_por_item: number;
  quantidade_venda: number;
  codigo_produto: number;
  cpf_funcionario: string;
  cpf_cliente: string;
}

type Props = {
  data: IVendas[];
};

function lista({ data }: Props) {
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
  const res = await fetch(`http://localhost:8080/vendas`);
  const data = await res.json();

  // Pass data to the page via props
  return { props: { data } };
}

export default lista;
