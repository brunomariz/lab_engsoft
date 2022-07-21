import React from "react";
import { FaCashRegister, FaList } from "react-icons/fa";
import LinkCard from "../../components/LinkCard/LinkCard";
import CardList from "../../components/CardList/CardList";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import { BsPerson } from "react-icons/bs";

type Props = {};

function Clientes({}: Props) {
  return (
    <SidebarLayout title="Clientes">
      <h2>O que você deseja fazer?</h2>
      <CardList>
        <LinkCard
          label="Cadastrar Cliente"
          icon={<BsPerson size={40}></BsPerson>}
          route="/clientes/cadastro"
        ></LinkCard>
        <LinkCard
          label="Listar Clientes"
          icon={<FaList size={40}></FaList>}
          route="/clientes/lista"
        ></LinkCard>
      </CardList>
    </SidebarLayout>
  );
}

export default Clientes;
