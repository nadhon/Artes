def calcular_total_despesas(despesas: list[dict]) -> float:
  """Calcula o total das despesas realizadas."""

  total = 0
  for despesa in despesas:

    total += despesa["valor"]

  return total

def calcular_valorpor_pessoa(total: float, quantidade: int) -> float:
  """Calcular o valor de quanto cada participante deveria pagar igualmente"""

  return total / quantidade

def calcular_gasto(participantes: list[str],
                   despesas: list[dict]) -> dict[str , float]:
                   "Calcula quanto cada participante pagou no total"

                   gastos = {}

                   for participante in participantes:
                    gastos[participante] = 0

                    for despesa in despesas:
                        pagador = despesa["pagador"]
                        valor = despesa["valor"]
                        if pagador in gastos:
                          gastos[pagador] += valor

                    return gastos