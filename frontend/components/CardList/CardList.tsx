import React, { ReactNode } from "react";

type Props = {
  children?: ReactNode | ReactNode[];
};

function CardList({ children }: Props) {
  return <div className="flex flex-wrap space-x-3">{children}</div>;
}

export default CardList;
