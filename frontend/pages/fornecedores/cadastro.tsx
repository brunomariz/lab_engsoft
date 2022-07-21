import React, { useState } from "react";
import CadastroClienteForm from "../../components/Forms/CadastroClienteForm/CadastroClienteForm";
import CadastroFornecedorForm from "../../components/Forms/CadastroFornecedorForm/CadastroFornecedorForm";
import VendaForm from "../../components/Forms/VendaForm/VendaForm";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";

type Props = {};

function Cadastro({}: Props) {
  return (
    <SidebarLayout title="Cadastrar Fornecedor">
      <h2 className="">Informações do Fornecedor</h2>
      <CadastroFornecedorForm></CadastroFornecedorForm>
    </SidebarLayout>
  );
}

export default Cadastro;
