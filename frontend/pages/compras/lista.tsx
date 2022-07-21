import React from "react";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import Table from "../../components/Table/Table";
import { mockPurchases } from "../../constants/mock/mockPurchases";
import { mockSales } from "../../constants/mock/mockSales";

interface ICompras {
  codigo_produto: number;
  CNPJ_fornecedor: string;
  quntidade_compra: number;
  data_compra: string;
  CPF_funcionario: string;
  valor_por_item: number;
}

type Props = {
  data: ICompras[];
};

function lista({ data }: Props) {
  return (
    <SidebarLayout title="Compras">
      <Table
        columnTitles={[
          "Código",
          "CNPJ Fornecedor",
          "Quantidade",
          "Data",
          "CPF Funcionario",
          "Valor",
        ]}
        items={data}
        title="Lista de Compras"
      ></Table>
    </SidebarLayout>
  );
}

// This gets called on every request
export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch(`http://localhost:8080/compra/listAll`);
  const data = await res.json();

  // Pass data to the page via props
  return { props: { data } };
}

export default lista;
