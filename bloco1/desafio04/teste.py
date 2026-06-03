import json
from datetime import datetime
from pathlib import Path
from typing import Any

logs_para_o_desafio: list[dict[str, Any]] = []

pasta_raiz = Path(__file__).parent
nome_arquivo = "log.jsonl"
caminho_arquivo = pasta_raiz / nome_arquivo


with open(caminho_arquivo, "r", encoding="utf-8") as file:
    for linha in file:
        if linha.strip():  # Garante que não vai ler linhas vazias
            dado = json.loads(linha)

            # Converte a string de volta para um objeto datetime real
            dado["timestamp"] = datetime.fromisoformat(dado["timestamp"])

            logs_para_o_desafio.append(dado)

logs_para_o_desafio_ordenado = sorted(logs_para_o_desafio, key=lambda x: x["timestamp"])

esquerda = 0
direita = len(logs_para_o_desafio_ordenado) - 1
meio = (esquerda + direita) // 2

print(logs_para_o_desafio_ordenado[0])

print(logs_para_o_desafio_ordenado[1])

print(logs_para_o_desafio_ordenado[2])

print(logs_para_o_desafio_ordenado[3])
