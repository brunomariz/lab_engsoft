import { useRouter } from "next/router";
import React, { useState } from "react";
import VendaForm from "../../components/Forms/VendaForm/VendaForm";
import SidebarLayout from "../../components/SidebarLayout/SidebarLayout";
import VendaConfirmation from "../../components/VendaConfirmation/VendaConfirmation";
import { postData } from "../../requests/postData";
import { IVendaValidation } from "../../validation/venda/vendaValidation";
import { IClientes } from "../clientes/lista";
import { IProduto } from "../produtos/lista";
import { IVendas } from "./lista";

type Props = {
  // vendaData: IVendas[];
  // productData: IProduto[];
  // clientData: IClientes[];
};

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
              values || { CPF_cliente: "", CPF_funcionario: "", produtos: [] }
            }
            handleConfirm={() => {
              console.log(values);
              postData(values || {}, "/venda/create");
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

// This gets called on every request
// export async function getServerSideProps() {
//   // Fetch data from external API
//   const vendaRes = await fetch(`http://localhost:8080/venda`);
//   const vendaData = await vendaRes.json();

//   const productRes = await fetch(`http://localhost:8080/produto/list`);
//   const productData = await productRes.json();

//   const clientRes = await fetch(`http://localhost:8080/client`);
//   const clientData = await clientRes.json();

//   // Pass data to the page via props
//   return { props: { vendaData, productData, clientData } };
// }

export default Vender;
