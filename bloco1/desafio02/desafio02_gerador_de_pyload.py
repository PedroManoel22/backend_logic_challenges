# Gerador de Payload de Pagamento (String de Pix Copia e Cola): Implemente a lógica para gerar a string EMV do Pix estático
#  (padrão BCB), calculando o CRC16 (Cyclic Redundancy Check) no final do payload.

from functions import PixStaticPayload

if __name__ == "__main__":
    pix = PixStaticPayload(
        pix_key="pedro123@gmail.com",
        merchant_name="Fulaninho de tal",
        merchant_city="São Paulo",
        amount=150.00,
    )

    pix_copia_e_cola = pix.generate()

    print("\n--- String Pix Copia e Cola ---\n")

    print(pix_copia_e_cola)

    # Validamos se o retorno é uma string e se começa com o padrão "000201"
    assert isinstance(pix_copia_e_cola, str), "Erro: O retorno deveria ser uma string"
    assert pix_copia_e_cola.startswith("000201"), (
        "Erro: O Pix deveria começar com 000201"
    )

    print("\nDesafio 02: Todos os testes passaram!")
