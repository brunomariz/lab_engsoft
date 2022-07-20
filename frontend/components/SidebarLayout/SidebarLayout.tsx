import React, { ReactNode } from "react";
import Sidebar from "../Sidebar/Sidebar";

type Props = {
  children?: ReactNode | ReactNode[];
  title: string;
};

function SidebarLayout({ children, title }: Props) {
  return (
    <>
      <Sidebar></Sidebar>
      <div className="pl-64 bg-white">
        <div className="w-full bg-gray-100">
          <h1 className="p-2 pl-4">{title}</h1>
        </div>
        <div className="bg-gray-100 h-full min-h-screen m-8 p-5">
          {children}
        </div>
      </div>
    </>
  );
}

export default SidebarLayout;
