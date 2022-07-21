import { object, string, ref, number, bool, array } from "yup";

export interface IVendaValidation {
  cpf_cliente: string;
  cpf_vendedor: string;
  produtos: {
    codigo_produto: string;
    quantidade_produto: number;
  }[];
}
// nome_produto: string;
// em_promocao: boolean;
// preco_venda: number;

export const vendaValidation = object().shape({
  cpf_cliente: string(),
  cpf_vendedor: string().required("Campo obrigatório"),
  produtos: array()
    .of(
      object().shape({
        codigo_produto: string(), //.required("Campo obrigatório"),
        // nome_produto: string().required("Campo obrigatório"),
        quantidade_produto: number().required("Campo obrigatório"),
        // em_promocao: bool(),
        // preco_venda: number().required("Campo obrigatório"),
      })
    )
    .required("Campo obrigatorio"),
});