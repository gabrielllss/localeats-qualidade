"""Regras de negocio relacionadas ao calculo de pedidos."""

TAXA_BASE_ENTREGA = 5.0
DISTANCIA_BASE_KM = 3.0
VALOR_POR_KM_EXCEDENTE = 2.0
TOTAL_MINIMO_ENTREGA_GRATIS = 100.0


def validar_item(item: dict) -> None:
    """Valida preco e quantidade de um item.

    Raises:
        ValueError: se o preco ou a quantidade nao forem positivos.
    """
    if item["preco"] <= 0:
        raise ValueError("O preco deve ser positivo.")

    if item["quantidade"] <= 0:
        raise ValueError("A quantidade deve ser positiva.")


def calcular_total(itens: list[dict]) -> float:
    """Calcula o total do pedido.

    Uma lista vazia resulta em total igual a zero.
    """
    total = 0

    for item in itens:
        validar_item(item)
        total += item["preco"] * item["quantidade"]

    return total


def calcular_taxa_entrega(distancia_km: float, total_pedido: float) -> float:
    """Calcula a taxa de entrega de um pedido.

    Regras:
        - ate 3 km, a taxa e R$ 5;
        - acima de 3 km, acrescentar R$ 2 por quilometro excedente;
        - pedidos a partir de R$ 100 possuem entrega gratuita.

    Raises:
        ValueError: se a distancia for negativa.
    """
    if distancia_km < 0:
        raise ValueError("A distancia nao pode ser negativa.")

    if total_pedido >= TOTAL_MINIMO_ENTREGA_GRATIS:
        return 0.0

    if distancia_km <= DISTANCIA_BASE_KM:
        return TAXA_BASE_ENTREGA

    km_excedente = distancia_km - DISTANCIA_BASE_KM
    return TAXA_BASE_ENTREGA + km_excedente * VALOR_POR_KM_EXCEDENTE
