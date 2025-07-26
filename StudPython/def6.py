# Avaliação de alunos "Verção 2"

def avaliar_nota(nome, nota1, nota2, nota3):
    #peso das notas
    peso1, peso2, peso3 = 2, 3, 5

    # Cálculo da média ponderada
    media = (nota1 * peso1 + nota2 * peso2 + nota3 *peso3) / (peso1 + peso2 + peso3)

    # Classificação  baseado na média
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    return {
        "nome": nome,
        "media": round(media, 2),
        "situacao": situacao
    }

# Função para garantir notas válidas 
def ler_nota(numero_nota):
    while True:
        try:
            nota = float(input(f"Digite a nota {numero_nota} (0 a 10):"))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota invalida! Digite entre 0 a 10")
        except ValueError:
            print("Entrada inválida! Use número com ponto (ex: 7.5)")

alunos = []

#loop de cadastro
while True:
    print("\n=== Cadastro de Aluno ===")
    nome = input("Digite o nome do aluno(a):")
    nota1 = ler_nota(1) 
    nota2 = ler_nota(2)
    nota3 = ler_nota(3)

    aluno = avaliar_nota(nome, nota1, nota2, nota3)
    alunos.append(aluno)

    continuar = input("Gostaria de cadastrar mais algum aluno(a): {s/n}")
    if continuar != 's':
        break

    print("\n=== Resultado Final ===")
    for aluno in alunos:
        print(f"\nNome: {aluno['nome']}")
        print(f"Media: {aluno['media']}")
        print(f"Situração: {aluno['situacao']}")
