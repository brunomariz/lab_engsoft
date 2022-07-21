import React from "react";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import Table from "../../components/Table/Table";
import { mockProducts } from "../../constants/mock/mockProdutos";

export interface IProduto {
  quantidade_produto: number;
  nome_produto: string;
  em_promocao: boolean;
  codigo_produto: number;
}

type Props = {
  data: IProduto[];
};

function Produtos({ data }: Props) {
  return (
    <SidebarLayout title="Produtos">
      <Table
        columnTitles={["Quantidade", "Nome", "Promoção", "Código"]}
        items={data.map((item) => {
          return {
            ...item,
            em_promocao: item.em_promocao ? "Sim" : "Não",
          };
        })}
        title="Lista de Produtos"
      ></Table>
    </SidebarLayout>
  );
}

// This gets called on every request
export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch(`http://localhost:8080/produto/list`);
  const data = await res.json();
  console.log(data);

  // Pass data to the page via props
  return { props: { data } };
}

export default Produtos;
