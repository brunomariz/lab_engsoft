import { useRouter } from "next/router";
import React, { useState } from "react";
import ProdutoForm from "../../components/Forms/ProdutoForm/ProdutoForm";
import VendaForm from "../../components/Forms/VendaForm/VendaForm";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import VendaConfirmation from "../../components/VendaConfirmation/VendaConfirmation";
import { IVendaValidation } from "../../validation/venda/vendaValidation";

type Props = {};

function Cadastro({}: Props) {
  const [step, setStep] = useState(0);
  const [values, setValues] = useState<IVendaValidation>();
  const router = useRouter();
  return (
    <SidebarLayout title="Cadastrar Produto">
      <h2 className="">Informações do Produto</h2>
      <ProdutoForm></ProdutoForm>
    </SidebarLayout>
  );
}

export default Cadastro;
