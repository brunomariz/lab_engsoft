import React from "react";
import VendaForm from "../../components/Forms/VendaForm/VendaForm";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";

type Props = {};

function Vender({}: Props) {
  return (
    <SidebarLayout title="Realizar Venda">
      <VendaForm></VendaForm>
    </SidebarLayout>
  );
}

export default Vender;
