import json
import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List


def generate_mock_logs(total_records: int = 100) -> List[Dict[str, Any]]:
    """Gera uma lista de logs textuais mockados em memória para o desafio.

    Os logs são gerados de forma desordenada e contêm timestamps com milissegundos.
    """
    levels = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"]
    messages = [
        "User authentication successful",
        "Database connection timeout, retrying...",
        "API request processed in 45ms",
        "Failed to upload profile picture",
        "Cache cleared for session token",
        "Disk usage reached 85%",
        "Inbound webhook received from gateway",
    ]

    base_time = datetime(2026, 6, 2, 8, 0, 0)  # Data de hoje simulada
    logs: list[dict[str, Any]] = []

    for i in range(total_records):
        # Gera offsets aleatórios de segundos e milissegundos para embaralhar o tempo
        random_seconds = random.randint(0, 3600)
        random_ms = random.randint(0, 999)
        timestamp = base_time + timedelta(
            seconds=random_seconds, milliseconds=random_ms
        )

        log_entry: dict[str, Any] = {
            "id": i + 1,
            "timestamp": timestamp,
            "level": random.choice(levels),
            "message": random.choice(messages),
        }

        logs.append(log_entry)

    random.shuffle(logs)
    return logs


if __name__ == "__main__":
    # Gerando 15 logs
    mocked_logs = generate_mock_logs(total_records=15)

    # print("--- EXEMPLO DOS LOGS GERADOS (DESORDENADOS) ---")
    # for log in mocked_logs:
    #     # Formatando o timestamp com milissegundos (%f) para exibição limpa
    #     time_str = log["timestamp"].strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    #     print(f"[{time_str}] {log['level']}: {log['message']} (ID: {log['id']})")

    # print(f"\nTotal de logs carregados em memória: {len(mocked_logs)}")
    # print("------------------------------------------------")

    pasta_raiz = Path(__file__).parent
    nome_arquivo = "log.jsonl"
    caminho_arquivo = pasta_raiz / nome_arquivo

    def serializador_data(mocked_logs: list[dict[str, Any]]):
        if isinstance(mocked_logs, datetime):
            return (
                mocked_logs.isoformat()
            )  # Retorna no padrão internacional "2026-06-02T08:36:39.136000"

        raise TypeError(f"Tipo {type(mocked_logs)} não é serializável")

    with open(caminho_arquivo, "w", encoding="utf-8") as file:
        for item in mocked_logs:
            print(item)
            json_line = json.dumps(item, default=serializador_data, ensure_ascii=False)

            file.write(json_line + "\n")
