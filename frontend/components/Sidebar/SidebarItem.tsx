import React, { ReactNode } from "react";

type Props = {
  label: string;
  icon: ReactNode;
};

function SidebarItem({ label, icon }: Props) {
  return (
    <button className="flex items-center justify-start text-gray-100 hover:bg-slate-700">
      <span className="p-1 pl-3">{icon}</span>
      <span className="p-1 text-lg pl-3">{label}</span>
    </button>
  );
}

export default SidebarItem;
