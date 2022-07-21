import React from "react";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import Table from "../../components/Table/Table";
import { mockCostumers } from "../../constants/mock/mockCostumers";

interface IClientes {
  nome_cliente: string;
  CPF_cliente: string;
}

type Props = {
  data: IClientes[];
};

function ListaClientes({ data }: Props) {
  return (
    <SidebarLayout title="Clientes">
      <Table
        columnTitles={["Nome", "CPF"]}
        items={data}
        title="Lista de Clientes"
      ></Table>
    </SidebarLayout>
  );
}

// This gets called on every request
export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch(`http://localhost:8080/client`);
  const data = await res.json();

  console.log(data);

  // Pass data to the page via props
  return { props: { data } };
}

export default ListaClientes;
