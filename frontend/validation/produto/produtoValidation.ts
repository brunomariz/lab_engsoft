import { object, string, ref, number, bool, array } from "yup";

export interface IProdutoValidation {
  nome_produto: string;
  quantidade_produto: number;
  em_promocao: boolean;
  preco_venda: number;
}

export const produtoValidation = object().shape({
  nome_produto: string().required("Campo obrigatório"),
  quantidade_produto: number().required("Campo obrigatório"),
  em_promocao: bool().required("Campo obrigatório"),
  preco_venda: number().required("Campo obrigatório"),
});
