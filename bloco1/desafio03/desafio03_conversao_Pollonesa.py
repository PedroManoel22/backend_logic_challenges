from my_stack import Stack

if __name__ == "__main__":
    my_stack = Stack()
    ex1 = ["2", "1", "+", "3", "*"]
    ex2 = ["3", "4", "*", "3", "+"]

    resultado1 = my_stack.expression_calculation(ex1)
    resultado2 = my_stack.expression_calculation(ex2)

    assert resultado1 == 9.0
    assert resultado2 == 15.0

    assert isinstance(resultado1, float)
    assert isinstance(resultado2, float)

    print(f"Todos os testes passaram! Resultado1: {resultado1}")
    print(f"Todos os testes passaram! Resultado2: {resultado2}")
