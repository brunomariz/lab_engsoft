import React, { ReactNode } from "react";
import Sidebar from "../Sidebar/Sidebar";

type Props = {
  children?: ReactNode | ReactNode[];
  title: string;
};

function SidebarLayout({ children, title }: Props) {
  return (
    <div>
      <Sidebar></Sidebar>
      <div className="pl-64">
        <div className="w-full bg-white">
          <h1 className="p-2 pl-4">{title}</h1>
        </div>
        <div className="bg-gray-200 h-full min-h-screen">{children}</div>
      </div>
    </div>
  );
}

export default SidebarLayout;
