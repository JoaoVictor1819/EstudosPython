# Desafio

# Cadastro de alunos com repetição 'while'

print("=== Cadastro de alunos ===")

alunos = []

while True:
    nome = input("\nDigite o nome do aluno(a):")
    idade = int(input("Digite a idade do mesmo:"))

    #Colocando 3 notas e armazenando em uma lista
    notas = []
    for i in range(3):
        nota = float(input(f"Digite a nota {i+1}:"))
        notas.append(nota)
    
    media = sum(notas) / len(notas)

    # Verifique a situação
    if media >= 7:
        situação = "Aprovado"
    elif media >= 5:
        situação = "Recuperação"
    else:
        situação = "Reprovado"

    # Criando dicionario 

    aluno = {
        "nome": nome,
        "idade": idade,
        "notas": notas,
        "media": media,
        "situacao": situação
    }

    alunos.append(aluno)

    # Pergunta se deseja continuar
    continuar = input("\nDeseja cadastras mais algum aluno(a)? (s/n):").lower()
    if continuar != "s":
        break

    # Exibindo todos os resultados
    print("\n=== Resultado Final ===")
    for aluno in alunos:
        print(f"\nNome: {aluno['nome']}")
        print(f"Idade {aluno['idade']}")
        print(f"Notas {aluno['notas']}")
        print(f"Media { aluno['media']:.2f}")
        print(f"Situação {aluno['situacao']}")