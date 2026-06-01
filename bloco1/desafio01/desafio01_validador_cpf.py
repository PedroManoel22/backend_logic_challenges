# Validador de CPF/CNPJ Profissional: Crie uma função que receba uma string, remova caracteres especiais,
# identifique se é CPF ou CNPJ e aplique o algoritmo de cálculo dos dígitos verificadores.

from functions import remove_caracteres_especiais

if __name__ == "__main__":
    assert remove_caracteres_especiais("001.129.800-66") is True

    assert remove_caracteres_especiais("001.129.800-12") is False

    assert remove_caracteres_especiais("56.116.412/0001-46") is True

    assert remove_caracteres_especiais("56.116.412/0001-45") is False

    print("\n\033[32mDesafio 01: Todos os testes passaram!\033[m\n")
