import { object, string, ref, number, bool, array } from "yup";

export interface ICadastroClienteValidation {
  cpf_cliente: string;
  nome_cliente: string;
}

export const cadastroClienteValidation = object().shape({
  cpf_cliente: string().required("Campo obrigatório"),
  nome_cliente: string().required("Campo obrigatório"),
});
