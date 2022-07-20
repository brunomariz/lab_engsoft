import Link from "next/link";
import React, { ReactNode } from "react";

type Props = {
  label: string;
  icon: ReactNode;
  route: string;
};

function SidebarItem({ label, icon, route }: Props) {
  return (
    <Link href={route}>
      <button className="flex items-center justify-start text-gray-100 hover:bg-slate-700 py-2 pl-2">
        <span className="">{icon}</span>
        <span className="text-lg pl-3">{label}</span>
      </button>
    </Link>
  );
}

export default SidebarItem;
