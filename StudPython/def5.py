# Desafio

def avaliar_aluno(nome, nota1, nota2, nota3):
       media = (nota1 + nota2 + nota3) / 3
        
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

alunos = []

while True:
    nome = input("Digite o nome do aluno(a):")
    n1 = float(input("Digite a primeira nota:"))
    n2 = float(input("Digite a segunda nota:"))
    n3 = float(input("Digite a tercira nota:"))

    aluno = avaliar_aluno(nome, n1, n2, n3)
    alunos.append(aluno)

    continuar = input("Gostaria de cadastrar mais alguma Aluno? {s/n}")
    if continuar != 's':
        break

    # Mostra os resultados
    print("\n=== Resultados Finais ===")
    print(f"\nNome do Aluno(a): {aluno['nome']}")
    print(f"Media: {aluno['media']}")
    print(f"Situação: {aluno['situacao']}")
              
              