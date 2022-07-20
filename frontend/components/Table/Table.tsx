import React from "react";

type Props = {
  items: object[];
  title: string;
  columnTitles: string[];
};

function Table({ items, title, columnTitles }: Props) {
  return (
    <>
      <h2 className="py-3">{title}</h2>
      <div
        className={`grid font-semibold text-slate-800 bg-gray-400 p-1 items-center`}
        style={{
          gridTemplateColumns: `repeat(${columnTitles.length}, 1fr)`,
        }}
      >
        {columnTitles.map((columnTitle) => {
          return <div className="p-1">{columnTitle}</div>;
        })}
      </div>
      {items.map((item, index) => {
        return (
          <div
            className={`grid p-1 ${index % 2 == 1 ? "bg-gray-200" : ""}`}
            style={{
              gridTemplateColumns: `repeat(${
                Object.entries(item).length
              }, 1fr)`,
            }}
          >
            {Object.entries(item).map((entry, index) => {
              const [key, value] = entry;
              return <div className="p-1">{value}</div>;
            })}
          </div>
        );
      })}
    </>
  );
}

export default Table;
