import React from "react";
import Sidebar from "../components/Sidebar/Sidebar";
import SidebarLayout from "../components/SidebarLayout/SidebarLayout";

type Props = {};

function Home({}: Props) {
  return <SidebarLayout title="Bem vindo, Funcionário"></SidebarLayout>;
}

export default Home;
