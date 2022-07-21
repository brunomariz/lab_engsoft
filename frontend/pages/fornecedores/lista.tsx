import React from "react";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import Table from "../../components/Table/Table";
import { mockCostumers } from "../../constants/mock/mockCostumers";
import { mockProviders } from "../../constants/mock/mockProviders";

interface IFornecedor {
  CNPJ_fornecedor: string;
  nome_fornecedor: string;
}

type Props = {
  data: IFornecedor[];
};

function ListaFornecedores({ data }: Props) {
  return (
    <SidebarLayout title="Fornecedores">
      <Table
        columnTitles={["Nome", "CNPJ"]}
        items={data}
        title="Lista de Fornecedores"
      ></Table>
    </SidebarLayout>
  );
}

// This gets called on every request
export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch(`http://localhost:8080/fornecedor`);
  const data = await res.json();
  console.log(data);

  // Pass data to the page via props
  return { props: { data } };
}
export default ListaFornecedores;
