import { useRouter } from "next/router";
import React, { useState } from "react";
import VendaForm from "../../components/Forms/VendaForm/VendaForm";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import VendaConfirmation from "../../components/VendaConfirmation/VendaConfirmation";
import { IVendaValidation } from "../../validation/venda/vendaValidation";

type Props = {};

function Vender({}: Props) {
  const [step, setStep] = useState(0);
  const [values, setValues] = useState<IVendaValidation>();
  const router = useRouter();
  return (
    <SidebarLayout title="Realizar Venda">
      {step == 0 ? (
        <>
          <h2 className="">Informações da Venda</h2>
          <VendaForm setStep={setStep} setValues={setValues}></VendaForm>
        </>
      ) : (
        <>
          <h2 className="">Confirmar Venda</h2>
          <VendaConfirmation
            values={
              values || { cpf_cliente: "", cpf_vendedor: "", produtos: [] }
            }
            handleConfirm={() => {
              console.log(values);
              router.push("/home");
            }}
            handleCancel={() => {
              console.log("venda cancelada");
              router.push("/home");
            }}
          ></VendaConfirmation>
        </>
      )}
    </SidebarLayout>
  );
}

export default Vender;
