import re


def remove_caracteres_especiais(string: str) -> bool | None:
    """Remove qualquer caractere não numérico de uma string e inicia a validação.

    Utiliza expressões regulares para filtrar o texto, garantindo que apenas
    dígitos sejam mantidos. Caso a string resultante seja puramente numérica,
    direciona o fluxo para a identificação do documento (CPF ou CNPJ).

    Args:
        string (str): A string original contendo o documento formatado
            (ex: "123.456.789-00").

    Returns:
        bool | None: Retorna True ou False dependendo da validação dos dígitos
            verificadores, ou None caso a entrada seja inválida.
    """

    string_limpa = re.sub(
        r"\D", "", string
    )  # remove qualquer caractere que não seja número

    if string_limpa.isdigit():
        return cpf_ou_cnpj(string_limpa)
    else:
        print("\nPor favor insira apenas número!\n")


def cpf_ou_cnpj(string: str) -> bool | None:
    """Identifica o tipo de documento pelo tamanho e direciona para validação.

    Verifica se a quantidade de caracteres numéricos corresponde a um CPF (11 dígitos)
    Análise do tamanho da string limpa para determinar se trata-se de um CPF
    (11 dígitos) ou CNPJ (14 dígitos), encaminhando para a respectiva função de cálculo.

    Args:
        string (str): String contendo apenas os números do documento.

    Returns:
        bool | None: Retorna o booleano resultante do cálculo dos dígitos
            verificadores, ou False/None se o tamanho for incorreto.
    """

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


def calculo_digito_verificadores_cpf(cpf: str) -> bool:
    """Calcula os dois dígitos verificadores de um CPF e valida o documento.

    A função replica o algoritmo oficial do Ministério da Fazenda para a validação
    de CPFs. O processo consiste em duas etapas de soma ponderada (com multiplicadores
    regressivos de 10 a 2 e de 11 a 2) sobre os dígitos da string base para determinar,
    através do resto da divisão por 11, o valor esperado para o primeiro e segundo
    dígitos verificadores.

    Args:
        cpf (str): String limpa (apenas números) com os 11 dígitos do CPF a ser validado.

    Returns:
        bool: Retorna True se os dígitos calculados corresponderem aos dígitos
            originais informados; retorna False caso contrário.
    """

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

    return cpf_verificador == cpf


def calculo_digito_verificadores_cnpj(cnpj: str) -> bool:
    """Calcula os dois dígitos verificadores de um CNPJ e valida o documento.

    Aplica o algoritmo de validação de CNPJ da Receita Federal. Realiza somas ponderadas
    utilizando duas listas distintas de multiplicadores fixos que ciclam de 5 a 2 e de
    9 a 2. O cálculo avalia o resto da divisão por 11 para definir se o dígito correspondente
    deve ser 0 (caso o resto seja menor que 2) ou o resultado da subtração (11 - resto).

    Args:
        cnpj (str): String limpa (apenas números) com os 14 dígitos do CNPJ a ser validado.

    Returns:
        bool: Retorna True se o CNPJ possuir dígitos verificadores matematicamente válidos;
            retorna False caso contrário.
    """

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

    return cnpj_verificador == cnpj
