# Validador de CPF/CNPJ Profissional: Crie uma função que receba uma string, remova caracteres especiais,
# identifique se é CPF ou CNPJ e aplique o algoritmo de cálculo dos dígitos verificadores.

import re


def remove_caracteres_especiais(string: str) -> str | None:
    string_limpa = re.sub(
        r"\D", "", string
    )  # remove qualquer caractere que não seja número
    if string_limpa.isdigit():
        return cpf_ou_cnpj(string_limpa)
    else:
        print("\nPor favor insira apenas número!\n")


def cpf_ou_cnpj(string: str):
    e_cpf = False
    e_cnpj = False

    if len(string) == 11:
        e_cpf = True

    elif len(string) == 14:
        e_cnpj = True

    if e_cpf:
        ...
    if e_cnpj:
        ...
