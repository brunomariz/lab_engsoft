import React from "react";
import { FaCashRegister, FaList } from "react-icons/fa";
import LinkCard from "../../components/LinkCard/LinkCard";
import CardList from "../../components/CardList/CardList";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";

type Props = {};

function Vendas({}: Props) {
  return (
    <SidebarLayout title="Vendas">
      <h2>O que você deseja fazer?</h2>
      <CardList>
        <LinkCard
          label="Realizar Venda"
          icon={<FaCashRegister size={40}></FaCashRegister>}
          route="/vendas/vender"
        ></LinkCard>
        <LinkCard
          label="Listar Vendas"
          icon={<FaList size={40}></FaList>}
          route="/vendas/lista"
        ></LinkCard>
      </CardList>
    </SidebarLayout>
  );
}

export default Vendas;
