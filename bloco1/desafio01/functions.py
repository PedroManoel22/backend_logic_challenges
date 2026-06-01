import re


def remove_caracteres_especiais(string: str) -> bool | None:
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
        return calculo_digito_verificadores_cpf(string)

    elif e_cnpj:
        return calculo_digito_verificadores_cnpj(string)

    else:
        print("\nA string tem que ter pelo menos 11 números para CPF e 14 para CNPJ")
        return False


def calculo_digito_verificadores_cpf(cpf: str):
    cpf_verificador = cpf[:9]
    multiplicador = 10
    soma = 0

    # Calcula o primeiro digito verificador
    for n in cpf_verificador:
        soma += int(n) * multiplicador
        multiplicador -= 1

    resto_divisao = soma % 11

    if resto_divisao == 0 or resto_divisao == 1:
        primeiro_digito_verificador = 0

    else:
        primeiro_digito_verificador = 11 - resto_divisao

    cpf_verificador += str(primeiro_digito_verificador)

    # Calcula o segundo digito verificador
    multiplicador = 11
    soma = 0

    for n in cpf_verificador:
        soma += int(n) * multiplicador
        multiplicador -= 1

    resto_divisao = soma % 11

    if resto_divisao == 0 or resto_divisao == 1:
        segundo_digito_verificador = 0

    else:
        segundo_digito_verificador = 11 - resto_divisao

    cpf_verificador += str(segundo_digito_verificador)

    if cpf_verificador == cpf:
        return True

    else:
        return False


def calculo_digito_verificadores_cnpj(cnpj: str):
    cnpj_verificador = cnpj[:12]
    multiplicadores = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    index_multiplicadores = 0

    for n in cnpj_verificador:
        soma += int(n) * multiplicadores[index_multiplicadores]
        index_multiplicadores += 1

    resto_divisao = soma % 11

    if resto_divisao < 2:
        primeiro_digito_verificador = 0

    else:
        primeiro_digito_verificador = 11 - resto_divisao

    cnpj_verificador += str(primeiro_digito_verificador)

    multiplicadores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    index_multiplicadores = 0

    for n in cnpj_verificador:
        soma += int(n) * multiplicadores[index_multiplicadores]
        index_multiplicadores += 1

    resto_divisao = soma % 11

    if resto_divisao < 2:
        segundo_digito_verificador = 0

    else:
        segundo_digito_verificador = 11 - resto_divisao

        cnpj_verificador += str(segundo_digito_verificador)

    if cnpj_verificador == cnpj:
        return True

    else:
        return False
