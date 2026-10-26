def mostrar_resumo(total: float, valor_por_pessoa: float) -> None:
  "Exibe o total gasto e o valor que cada pessoa deveira pagar"

  print("-----------------------------------------------")
  print("-------------------RESUMO----------------------")
  print("-----------------------------------------------")

  print(f"Total gasto: R$ {total:.2f}")
  print(f"Valor por pessoa: R$ {valor_por_pessoa:.2f}")

def mostrar_gastos(gastos: dict[str, float]) -> None:
  "Exibe quanto cada participante pagou."


  print("-----------------------------------------------")
  print("-------------------GASTOS----------------------")
  print("-----------------------------------------------")

  for participante, valor in gastos.items():
    print(f"{participante}: R$ {valor:.2f}")

def mostrar_saldo(saldos: dict[str, float]) -> None:
  "Exibe o saldo de cada participante individualmente."

  print("-----------------------------------------------")
  print("-------------------SALDO-----------------------")
  print("-----------------------------------------------")

  for participante in saldos:

    saldo = saldos[participante]

    if saldo > 0:
      print(
          f"{participante}: + R$ {saldo:.2f}"
          "deve receber"
      )
    elif saldo <0:

      print(
          f"{participante}: - R$ {saldo:.2f} "
          "deve pagar"
      )

    else:
      print(f"{participante}: R$ 0.00 está quite")