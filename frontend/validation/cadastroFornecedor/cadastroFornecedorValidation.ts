import { object, string, ref, number, bool, array } from "yup";

export interface ICadastroFornecedorValidation {
  cnpj_fornecedor: string;
  nome_fornecedor: string;
}

export const cadastroFornecedorValidation = object().shape({
  cnpj_fornecedor: string().required("Campo obrigatório"),
  nome_fornecedor: string().required("Campo obrigatório"),
});
