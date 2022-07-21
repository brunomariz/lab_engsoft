import React from "react";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import Table from "../../components/Table/Table";
import { mockProducts } from "../../constants/mock/mockProdutos";

interface IProduto {
  nome_produto: string;
  quantidade_produto: number;
  em_promocao: boolean;
  preco_venda: number;
}

type Props = {
  data: IProduto[];
};

function Produtos({ data }: Props) {
  return (
    <SidebarLayout title="Produtos">
      <Table
        columnTitles={["Código", "Nome", "Quantidade", "Promoção", "Preço"]}
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
  const res = await fetch(`http://localhost:8080/produto`);
  const data = await res.json();
  console.log(data);

  // Pass data to the page via props
  return { props: { data } };
}

export default Produtos;
