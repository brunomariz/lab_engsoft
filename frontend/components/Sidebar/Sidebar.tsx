import React from "react";
import SidebarItem from "./SidebarItem";
import {
  FaMoneyBill,
  FaBarcode,
  FaSalesforce,
  FaAcquisitionsIncorporated,
  FaCashRegister,
} from "react-icons/fa";

type Props = {};

function Sidebar({}: Props) {
  return (
    <div className="h-screen fixed left-0 top-0 w-64 bg-slate-900 flex flex-col">
      <SidebarItem
        icon={<FaMoneyBill size={30} />}
        label="Finanças"
      ></SidebarItem>
      <SidebarItem
        icon={<FaBarcode size={30} />}
        label="Produtos"
      ></SidebarItem>
      <SidebarItem
        icon={<FaCashRegister size={30} />}
        label="Vendas"
      ></SidebarItem>
    </div>
  );
}

export default Sidebar;
