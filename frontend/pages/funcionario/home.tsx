import React from "react";
import Sidebar from "../../components/Sidebar/Sidebar";

type Props = {};

function Home({}: Props) {
  return (
    <div>
      <Sidebar></Sidebar>
      <h1 className="pl-64">Bem vindo, Funcionário</h1>
    </div>
  );
}

export default Home;
