import React from "react";
import SidebarItem from "./SidebarItem";
import {
  FaMoneyBill,
  FaBarcode,
  FaSalesforce,
  FaAcquisitionsIncorporated,
  FaCashRegister,
  FaHome,
} from "react-icons/fa";
import { BsFillPersonFill } from "react-icons/bs";

type Props = {};

function Sidebar({}: Props) {
  return (
    <div className="h-screen fixed left-0 top-0 w-64 bg-slate-900 flex flex-col">
      <SidebarItem
        icon={<FaHome size={30} />}
        label="Home"
        route="/home"
      ></SidebarItem>
      <SidebarItem
        icon={<FaMoneyBill size={30} />}
        label="Finanças"
        route="/financas"
      ></SidebarItem>
      <SidebarItem
        icon={<FaBarcode size={30} />}
        label="Produtos"
        route="/produtos"
      ></SidebarItem>
      <SidebarItem
        icon={<FaCashRegister size={30} />}
        label="Vendas"
        route="/vendas"
      ></SidebarItem>
      <SidebarItem
        icon={<BsFillPersonFill size={30} />}
        label="Vendedores Ativos"
        route="/vendedores"
      ></SidebarItem>
    </div>
  );
}

export default Sidebar;
