from participantes import cadastrar_participantes
from despesas import cadastrar_despesas
from calculos import (
    calcular_total,
    calcular_valorpor_pessoa,
    calcular_gasto,
    calcular_saldo
)
from relatorios import (
    mostrar_resumo,
    mostrar_gastos,
    mostrar_saldo
)

def main() -> None:

  "Execução do sistema de divisão de despesas"

  print("Evento de Splitwise genérico")

  quantidade_participantes = int(
      input("Digite a quantidade de participantes: ")
  )
  participantes = cadastrar_participantes(
      quantidade_participantes
  )

  quantidade_despesas = int(
      input("Digite a quantidade de despesas: ")
  )
  despesas = cadastrar_despesas(
      quantidade_despesas
  )

  total = calcular_total(despesas)

  valor_por_pessoa = calcular_valorpor_pessoa(
      total,
      quantidade_participantes
  )

  gastos = calcular_gasto(
      participantes,
      despesas
  )

  saldos = calcular_saldo(
      gastos,
      valor_por_pessoa
  )

  mostrar_resumo(
      total,
      valor_por_pessoa
  )
  mostrar_gastos(
      gastos
  )
  mostrar_saldo(
      saldos
  )

if __name__ == "__main__":
  main()