# Registro do ciclo de TDD

Funcao implementada: `calcular_taxa_entrega(distancia_km, total_pedido)` em `src/pedido.py`.

## Ciclo 1 — taxa base ate 3 km

**Teste criado:** `test_cobra_taxa_base_para_entrega_ate_3_km` (2 km e pedido de R$ 50 devem gerar taxa de R$ 5).

**Red:** `ImportError: cannot import name 'calcular_taxa_entrega'` — a funcao ainda nao existia, entao o teste nem podia ser coletado.

**Green:** implementacao minima retornando `5` fixo. Suite: 5 passed.

**Refactor:** nao foi necessario neste ciclo.

## Ciclo 2 — acrescimo por quilometro excedente

**Teste criado:** `test_acrescenta_2_reais_por_km_excedente_acima_de_3_km` (4 km e pedido de R$ 50 devem gerar taxa de R$ 7).

**Red:** `assert 5 == 7` — a funcao ainda cobrava sempre a taxa base.

**Green:** `taxa = 5` e, quando `distancia_km > 3`, somar `(distancia_km - 3) * 2`. Suite: 6 passed.

**Refactor:** nao foi necessario neste ciclo.

## Ciclo 3 — entrega gratuita

**Teste criado:** `test_entrega_gratuita_para_pedidos_a_partir_de_100_reais` (5 km e pedido de R$ 100 devem gerar taxa de R$ 0).

**Red:** `assert 9 == 0` — a funcao calculava a taxa por distancia mesmo com pedido acima de R$ 100.

**Green:** retornar `0` quando `total_pedido >= 100`, antes de calcular a taxa por distancia. Suite: 7 passed.

**Refactor:** nao foi necessario neste ciclo.

## Ciclo 4 (desafio opcional) — distancia negativa

**Teste criado:** `test_rejeita_distancia_negativa` (distancia `-1` deve gerar `ValueError`).

**Red:** `Failed: DID NOT RAISE ValueError`.

**Green:** validacao `if distancia_km < 0: raise ValueError(...)`. Suite: 8 passed.

**Refactor:** nao foi necessario neste ciclo.

## Refactor final

- Extraidas as constantes `TAXA_BASE_ENTREGA`, `DISTANCIA_BASE_KM`, `VALOR_POR_KM_EXCEDENTE` e `TOTAL_MINIMO_ENTREGA_GRATIS`, eliminando numeros soltos no codigo.
- Docstring da funcao atualizada com as tres regras e a excecao, e assinatura tipada.
- Comportamento preservado: a suite continuou com 8 testes aprovados.

**Resultado final:** 8 passed — ver `relatorio-testes.txt`.
