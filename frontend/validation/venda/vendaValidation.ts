import { object, string, ref, number, bool, array } from "yup";

export interface IVendaValidation {
  CPF_cliente: string;
  CPF_funcionario: string;
  produtos: {
    codigo_produto: string;
    quantidade: number;
    valor: number;
  }[];
}
// nome_produto: string;
// em_promocao: boolean;
// preco_venda: number;

export const vendaValidation = object().shape({
  CPF_cliente: string(),
  CPF_funcionario: string().required("Campo obrigatório"),
  produtos: array()
    .of(
      object().shape({
        codigo_produto: string(), //.required("Campo obrigatório"),
        // nome_produto: string().required("Campo obrigatório"),
        quantidade: number().required("Campo obrigatório"),
        valor: number().required("Campo obrigatório"),

        // em_promocao: bool(),
        // preco_venda: number().required("Campo obrigatório"),
      })
    )
    .required("Campo obrigatorio"),
});
