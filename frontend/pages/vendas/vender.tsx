import React, { useState } from "react";
import VendaForm from "../../components/Forms/VendaForm/VendaForm";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";

type Props = {};

function Vender({}: Props) {
  return (
    <SidebarLayout title="Realizar Venda">
      <h2 className="">Informações da Venda</h2>
      <VendaForm></VendaForm>
    </SidebarLayout>
  );
}

export default Vender;
