import Link from "next/link";
import React, { ReactNode } from "react";
import { FaList } from "react-icons/fa";

type Props = {
  label: string;
  icon: ReactNode;
  route: string;
};

function LinkCard({ label, icon, route }: Props) {
  return (
    <div className="cursor-pointer hover:scale-110 transition-all delay-50">
      <Link href={route}>
        <div className="bg-slate-900 text-gray-50 rounded-lg p-8 flex items-center justify-center">
          <div className="flex flex-col items-center">
            <span className="p-2">{label}</span>
            <div className="p-8">{icon}</div>
          </div>
        </div>
      </Link>
    </div>
  );
}

export default LinkCard;
