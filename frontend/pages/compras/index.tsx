import React from "react";
import { FaCashRegister, FaList } from "react-icons/fa";
import LinkCard from "../../components/LinkCard/LinkCard";
import CardList from "../../components/CardList/CardList";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";

type Props = {};

function Compras({}: Props) {
  return (
    <SidebarLayout title="Compras">
      <h2>O que você deseja fazer?</h2>
      <CardList>
        <LinkCard
          label="Realizar Compra"
          icon={<FaCashRegister size={40}></FaCashRegister>}
          route="/compras/comprar"
        ></LinkCard>
        <LinkCard
          label="Listar Compras"
          icon={<FaList size={40}></FaList>}
          route="/compras/lista"
        ></LinkCard>
      </CardList>
    </SidebarLayout>
  );
}

export default Compras;
