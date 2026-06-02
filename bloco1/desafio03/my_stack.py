# Conversor de Notação Polonesa Inversa (RPN): Implemente uma calculadora baseada em pilha (Stack) que
# resolva expressões matemáticas em formato RPN (ex: ["2", "1", "+", "3", "*"] -> 9).

import operator
from collections import deque
from typing import Any, Optional


class Stack:
    def __init__(self) -> None:
        self._items: deque[Any] = deque()

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        """Remove e retorna o item do topo da pilha.

        Raises:
            IndexError: Se a pilha estiver vazia.
        """
        try:
            return self._items.pop()
        except IndexError:
            raise IndexError("pop de uma pilha vazia") from None

    def peek(self) -> Optional[Any]:
        """Retorna o item do topo sem removê-lo. Retorna None se vazia."""
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        """Verifica se a pilha está vazia."""
        return len(self._items) == 0

    def put_on_top(self, values: list[str]):
        for x in values:
            self._items.append(x)

        return self._items

    def __len__(self) -> int:
        """Permite usar len(stack) de forma Pythônica."""
        return len(self._items)

    def __repr__(self) -> str:
        """Representação limpa do objeto para debugging."""
        return f"Stack({list(self._items)})"

    def expression_calculation(self, values: list[str]):
        OPERATORS: dict[str, Any] = {  # type: ignore
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,  # type: ignore
        }

        for x in values:
            if x in OPERATORS:
                operand_b = float(self.pop())
                operand_a = float(self.pop())

                # executa a operação de acordo com o símbolo
                result = OPERATORS[x](operand_a, operand_b)

                # Empilha o resultado de volta para ser usado no próximo cálculo
                self.push(result)
            else:
                self.push(x)

        return float(self.pop())
