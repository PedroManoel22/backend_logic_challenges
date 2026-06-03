from typing import Any


class BuscaBinaria:
    def __init__(self, lista: list[dict[str, Any]], alvo: int) -> None:
        self.lista = lista
        self.alvo = alvo

    def buscar(self):
        esquerda = 0
        direita = len(self.lista) - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            id_atual = self.lista[meio]["id"]

            if id_atual == self.alvo:
                print(f"Elemento com id {self.alvo} encontrado!")
                return f"{self.lista[meio]}"

            elif self.alvo < id_atual:
                direita = meio - 1  # descarta metade direita

            else:
                esquerda = meio + 1  # descarta metade esquerda

        print(f"Elemento com id {self.alvo} não encontrado")
        return None
