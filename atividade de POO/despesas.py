def cadastrar_despesas(quantidade: int) -> list[dict]:
  """Cadastro das despesas Realizadas durante o evento."""

  despesas = []

  for despesa in range(quantidade):
    print("----------------------------")
    print("Digite os dados da despesa")
    print("----------------------------")

    pagador = input(" Quem pagou? ")
    valor = float(input("Valor da despesa: R$ "))
    descricao = input("Descrição da despesa: ")
    categoria = input("Categoraia: ")
    despesa = {
        "pagador": pagador,
        "valor": valor,
        "descricao": descricao,
        "categoria": categoria
        }

    despesas.append(despesa)

  return despesas