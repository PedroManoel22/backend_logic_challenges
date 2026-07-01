# 05 Algoritmo de Rate Limiting (Token Bucket): Implemente em Python puro a lógica do algoritmo Token Bucket para controlar
#  o limite de requisições por IP (ex: 5 requisições por minuto).

import time
from dataclasses import dataclass, field


@dataclass
class Bucket:
    """Representa o balde de tokens para um IP específico."""

    capacity: int
    refill_rate: float  # Quantidade de tokens adicionados por segundo
    tokens: float = 0.0
    last_update: float = field(default_factory=time.time)

    def __post_init__(self) -> None:
        # O balde começa cheio
        self.tokens = float(self.capacity)


class TokenBucketLimiter:
    def __init__(self, capacity: int, period_in_seconds: int) -> None:
        """
        Gerenciador de Rate Limiting usando o algoritmo Token Bucket.

        :param capacity: Número máximo de requisições permitidas no período (tamanho do balde).
        :param period_in_seconds: Janela de tempo em segundos para a taxa de recarga.
        """
        self.capacity = capacity
        # Calcula quantos tokens são gerados por segundo (ex: 5 tokens / 60s = 0.083 tokens/s)
        self.refill_rate = capacity / period_in_seconds
        self._ip_buckets: dict[str, Bucket] = {}

    def _get_or_create_bucket(self, ip: str) -> Bucket:
        """Recupera o balde do IP ou cria um novo caso não exista."""
        # Adicione o underline antes de ip_buckets bem aqui:
        if ip not in self._ip_buckets:
            self._ip_buckets[ip] = Bucket(
                capacity=self.capacity, refill_rate=self.refill_rate
            )
        return self._ip_buckets[ip]

    def _refill_tokens(self, bucket: Bucket) -> None:
        """Atualiza a quantidade de tokens no balde com base no tempo decorrido."""
        now = time.time()
        elapsed_time = now - bucket.last_update

        # Incrementa os tokens proporcionalmente ao tempo passado
        new_tokens = elapsed_time * bucket.refill_rate
        bucket.tokens = min(bucket.capacity, bucket.tokens + new_tokens)
        bucket.last_update = now

    def allow_request(self, ip: str) -> bool:
        """
        Verifica se a requisição do IP pode ser processada.
        Consome 1 token se disponível.
        """
        bucket = self._get_or_create_bucket(ip)
        self._refill_tokens(bucket)

        if bucket.tokens >= 1.0:
            bucket.tokens -= 1.0
            return True

        return False


# --- Exemplo de Uso e Demonstração Prática ---
if __name__ == "__main__":
    # Configuração do desafio: 5 requisições por minuto (60 segundos)
    limiter = TokenBucketLimiter(capacity=5, period_in_seconds=60)
    client_ip = "192.168.1.50"

    print("--- Testando Rajada de Requisições (Burst) ---")
    for i in range(1, 8):
        allowed = limiter.allow_request(client_ip)
        status = "✅ Permitida" if allowed else "❌ Bloqueada (Rate Limit Exceeded)"
        print(f"Requisição {i}: {status}")

    print("\n--- Aguardando 12 segundos para recuperar 1 token... ---")
    # Como a taxa é 5 tokens por 60s, recuperamos 1 token a cada 12 segundos (60 / 5)
    time.sleep(12)

    allowed = limiter.allow_request(client_ip)
    status = "✅ Permitida" if allowed else "❌ Bloqueada"
    print(f"Requisição após espera: {status}")
