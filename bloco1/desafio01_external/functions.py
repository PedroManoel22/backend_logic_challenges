import re

from validate_docbr import CNPJ, CPF

cpf_validador = CPF()
cnpj_validador = CNPJ()


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
        return cpf_validador.validate(string)

    elif e_cnpj:
        return cnpj_validador.validate(string)

    else:
        print("\nA string tem que ter pelo menos 11 números para CPF e 14 para CNPJ")
        return False
