import { useRouter } from "next/router";
import React, { useState } from "react";
import CompraConfirmation from "../../components/CompraConfirmation/CompraConfirmation";
import CompraForm from "../../components/Forms/CompraForm/CompraForm";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import { ICompraValidation } from "../../validation/compra/compraValidation";

type Props = {};

function Vender({}: Props) {
  const [step, setStep] = useState(0);
  const [values, setValues] = useState<ICompraValidation>();
  const router = useRouter();
  return (
    <SidebarLayout title="Realizar Compra">
      {step == 0 ? (
        <>
          <h2 className="">Informações da Compra</h2>
          <CompraForm setStep={setStep} setValues={setValues}></CompraForm>
        </>
      ) : (
        <>
          <h2 className="">Confirmar Venda</h2>
          <CompraConfirmation
            values={
              values || { cnpj_fornecedor: "", cpf_vendedor: "", produtos: [] }
            }
            handleConfirm={() => {
              console.log(values);
              fetch("http://localhost:8080/compras", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify(values),
              });
              router.push("/home");
            }}
            handleCancel={() => {
              console.log("compra cancelada");
              router.push("/home");
            }}
          ></CompraConfirmation>
        </>
      )}
    </SidebarLayout>
  );
}

export default Vender;
