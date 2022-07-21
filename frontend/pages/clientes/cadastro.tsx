import React, { useState } from "react";
import CadastroClienteForm from "../../components/Forms/CadastroClienteForm/CadastroClienteForm";
import VendaForm from "../../components/Forms/VendaForm/VendaForm";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";

type Props = {};

function Cadastro({}: Props) {
  return (
    <SidebarLayout title="Cadastrar Cliente">
      <h2 className="">Informações do Cliente</h2>
      <CadastroClienteForm></CadastroClienteForm>
    </SidebarLayout>
  );
}

export default Cadastro;
