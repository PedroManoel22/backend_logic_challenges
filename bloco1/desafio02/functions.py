from dataclasses import dataclass
from typing import Optional

import crcmod

_crc16_func = crcmod.mkCrcFun(poly=0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)  # type: ignore


def _calcular_crc16(data: bytes) -> int:
    """Calcula o CRC16 de um bloco de bytes usando o padrão CCITT-FALSE."""
    return _crc16_func(data)  # type: ignore


@dataclass
class PixStaticPayload:
    """Responsável por estruturar e gerar o payload do Pix Estático (EMV)."""

    pix_key: str
    merchant_name: str
    merchant_city: str
    txid: str = "***"  # identificador da transação
    amount: Optional[float] = None

    def _format_field(self, field_id: str, value: str) -> str:
        """Formata um campo no padrão EMV: ID (2 dig) + Tamanho (2dig) + valor."""
        size = str(len(value)).zfill(2)
        return f"{field_id}{size}{value}"

    def _generate_merchant_account_info(self) -> str:
        """Gera o bloco de informações da conta do comerciante (ID 26)."""
        gui = self._format_field("00", "br.gov.bcb.pix")
        key = self._format_field("01", self.pix_key)
        return self._format_field("26", f"{gui}{key}")

    def _generate_additional_data_field(self) -> str:
        """Gera o bloco de dados adicionais (ID 62), contendo o TXID."""
        txid_field = self._format_field("05", self.txid)
        return self._format_field("62", txid_field)

    def _calculate_crc16(self, payload: str) -> str:
        """Calcula o CRC16 (Polinômio 0x1021, Init 0xFFFF) no padrão CCITT-FALSE."""
        # O padrão do Pix exige o cálculo em cima da string convertida para bytes (utf-8)

        crc_value = _calcular_crc16(payload.encode("UTF-8"))

        # Retorna o hex em maiúsculo, formatado com 4 casas e zeros à esquerda
        return f"{crc_value:04X}"

    def generate(self) -> str:
        """Compila todos os campos e gera a string final do Pix Copia e Cola."""
        lines = [
            self._format_field("00", "01"),  # Payload Format Indicator
            self._generate_merchant_account_info(),  # Merchant Account Info (ID 26)
            self._format_field("52", "0000"),  # Merchant Category Code
            self._format_field("53", "986"),  # Transaction Currency (BRL = 986)
        ]

        if self.amount is not None:
            # Formata o valor com 2 casas decimais (ex: 10.50)
            amount_str = f"{self.amount:.2f}"
            lines.append(self._format_field("54", amount_str))

        lines.extend(
            [
                self._format_field("58", "BR"),  # Country Code
                self._format_field(
                    "59", self.merchant_name[:25]
                ),  # Merchant Name (Max 25 char)
                self._format_field(
                    "60", self.merchant_city[:15]
                ),  # Merchant City (Max 15 char)
                self._generate_additional_data_field(),  # Additional Data Field (TXID)
            ]
        )

        # Junta todo o payload construído até aqui
        partial_payload = "".join(lines)

        # Adiciona o ID do CRC (63) e o tamanho do CRC (04) para o cálculo final
        payload_to_crc = f"{partial_payload}6304"

        # Calcula o CRC16 e monta a string final
        crc16 = self._calculate_crc16(payload_to_crc)
        return f"{payload_to_crc}{crc16}"
