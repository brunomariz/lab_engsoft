import React from "react";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import Table from "../../components/Table/Table";
import { mockPurchases } from "../../constants/mock/mockPurchases";
import { mockSales } from "../../constants/mock/mockSales";

interface ICompras {
  id_compra: number;
  quantidade_compra: number;
  CPF_funcionario: string;
  codigo_produto: number;
  data_compra: string;
  CNPJ_fornecedor: string;
}

type Props = {
  data: ICompras[];
};

function lista({ data }: Props) {
  return (
    <SidebarLayout title="Compras">
      <Table
        columnTitles={[
          "ID",
          "Quantidade",
          "CPF Funcionario",
          "Código",
          "Data",
          "CNPJ Fornecedor",
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
