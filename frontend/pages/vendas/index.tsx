import React from "react";
import { FaList } from "react-icons/fa";
import LinkCard from "../../components/LinkCard/LinkCard";
import CardList from "../../components/CardList/CardList";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";

type Props = {};

function Vendas({}: Props) {
  return (
    <SidebarLayout title="Vendas">
      <CardList>
        <LinkCard
          label="Realizar Venda"
          icon={<FaList size={40}></FaList>}
          route="/vendas/vender"
        ></LinkCard>
        <LinkCard
          label="Lista de Vendas"
          icon={<FaList size={40}></FaList>}
          route="/vendas/lista"
        ></LinkCard>
      </CardList>
    </SidebarLayout>
  );
}

export default Vendas;
