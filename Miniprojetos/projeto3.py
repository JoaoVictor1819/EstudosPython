# Desafio

# Cadastro e avaliação de participantes em um evento

participantes = []

while True:
    print("\n=== Cadastro dos participantes ===")


    nome = input("Digite o nome do participante:")
    idade = int(input("Digite a idade do participante:"))

    # Verificar sé esta na faixa permitida(opcional)
    if idade < 14 or idade >30:
        print("Idade fora do permitido para participar (14 a 30 anos).")
        continuar = input("Deseja cadastrar outro participante? (s/n):")
        if continuar != 's':
            break
        else:
            continue

    notas = []
    for i in range(3):
        nota = float(input(f"Digite a nota {i+1}:"))
        notas.append(nota)

    media = sum(notas) / len(notas)

    # Verifique situação com if, elif e else
    if media >= 7:
        situacao = "aprovado"
    elif media >= 5:
        situacao = "recuperacao"
    else:
        situacao = "reprovado"

    # Criando um dicionario

    participante = {
        "nome": nome,
        "idade": idade,
        "notas": notas,
        "media": media,
        "situacao":situacao
    }

    participantes.append(participante)

    continuar = input("Deseja cadastrar mais algum participante? {s/n}").lower()
    if continuar != 's':
     break

    # Exibir o resultado final
    print("\n==== Participantes Cadastrado ====")
    for p in participantes:
        print(f"{p['nome']}, idade:{p['idade']}, notas: {p['notas']}, media: {p['media']:.2f} Situação: {p['situacao']}")