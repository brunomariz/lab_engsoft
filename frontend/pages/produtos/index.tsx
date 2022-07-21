import React from "react";
import { FaCashRegister, FaList } from "react-icons/fa";
import LinkCard from "../../components/LinkCard/LinkCard";
import CardList from "../../components/CardList/CardList";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";

type Props = {};

function Produtos({}: Props) {
  return (
    <SidebarLayout title="Produtos">
      <h2>O que você deseja fazer?</h2>
      <CardList>
        <LinkCard
          label="Cadastrar Produto"
          icon={<FaCashRegister size={40}></FaCashRegister>}
          route="/produtos/cadastro"
        ></LinkCard>
        <LinkCard
          label="Listar Produtos"
          icon={<FaList size={40}></FaList>}
          route="/produtos/lista"
        ></LinkCard>
      </CardList>
    </SidebarLayout>
  );
}

export default Produtos;
