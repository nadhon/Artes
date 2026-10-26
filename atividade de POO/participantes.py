def cadastrar_participantes(quantidade: int) -> list[str]:
  """ Cadastra os nomes dos participantes do evento."""
  participante = []
  for pessoas in range(quantidade):
    quantidade = int(input("Digite a quantidade de participantes: "))
    participante.append(input("Digite seu nome: "))

  return participante