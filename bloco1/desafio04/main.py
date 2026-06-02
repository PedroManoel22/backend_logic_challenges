# Filtro Avançado de Logs com Busca Binária: Dado um arquivo de log textual gigante (mockado em memória),
# ordene-o por timestamp e implemente uma busca binária para encontrar eventos ocorridos em um intervalo exato de milissegundos.

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
