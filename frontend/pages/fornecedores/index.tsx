import React from "react";
import { FaCashRegister, FaList } from "react-icons/fa";
import LinkCard from "../../components/LinkCard/LinkCard";
import CardList from "../../components/CardList/CardList";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import { BsPerson } from "react-icons/bs";

type Props = {};

function Fornecedores({}: Props) {
  return (
    <SidebarLayout title="Fornecedores">
      <h2>O que você deseja fazer?</h2>
      <CardList>
        <LinkCard
          label="Cadastrar Fornecedor"
          icon={<BsPerson size={40}></BsPerson>}
          route="/fornecedores/cadastro"
        ></LinkCard>
        <LinkCard
          label="Listar Fornecedores"
          icon={<FaList size={40}></FaList>}
          route="/fornecedores/lista"
        ></LinkCard>
      </CardList>
    </SidebarLayout>
  );
}

export default Fornecedores;
