import { object, string, ref, number, bool, array } from "yup";

export interface ICadastroClienteValidation {
  CPF_cliente: string;
  nome_cliente: string;
}

export const cadastroClienteValidation = object().shape({
  CPF_cliente: string().required("Campo obrigatório"),
  nome_cliente: string().required("Campo obrigatório"),
});
