import React from "react";
import SidebarLayout from "../components/SidebarLayout/SidebarLayout";
import Table from "../components/Table/Table";
import { mockEmployees } from "../constants/mock/mockEmployees";

interface IFuncionarios {
  CPF_funcionario: string;
  eh_gerente: boolean;
  nome_funcionario: string;
  salario_fixo: number;
  login_usuario: string;
}

type Props = { data: IFuncionarios[] };

function Vendedores({ data }: Props) {
  return (
    <SidebarLayout title="Vendedores Ativos">
      <Table
        columnTitles={["CPF", "Cargo", "Nome", "Salario Fixo", "Usuario"]}
        items={data.map((item) => {
          return {
            ...item,
            eh_gerente: item.eh_gerente ? "Gerente" : "Funcionario",
          };
        })}
        title="Lista de Vendedores Ativos"
      ></Table>
    </SidebarLayout>
  );
}

// This gets called on every request
export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch(`http://localhost:8080/funcionario`);
  const data = await res.json();
  console.log(data);

  // Pass data to the page via props
  return { props: { data } };
}

export default Vendedores;
