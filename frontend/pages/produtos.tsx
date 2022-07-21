import React from "react";
import SidebarLayout from "../components/SidebarLayout/SidebarLayout";
import Table from "../components/Table/Table";
import { mockProducts } from "../constants/mock/mockProdutos";

type Props = {};
function Produtos({}: Props) {
  return (
    <SidebarLayout title="Produtos">
      <Table
        columnTitles={["Código", "Nome", "Quantidade", "Promoção", "Preço"]}
        items={mockProducts.map((item) => {
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

export default Produtos;
