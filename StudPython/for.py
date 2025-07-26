# Desafio de "for" em python

# Cadastra o boletim de 2 alunos

# Lista para guardar dados dos alunos
alunos = []

# Repetição para cadastra 2 alunos
for i in range(2):
    print(f"\nCadastro do {i+1} aluno:")
    nome = input("Digite o nome:")

    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))

    media = (nota1 + nota2) / 2

#verifique a situação
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

# Crindo um dicionario dos alunos

    aluno = {
        "nome":  nome,
        "notas": [nota1, nota2],
        "media": media,
        "situacao": situacao
    }

# Adiciona o aluno a lista
    alunos.append(aluno)

# Mostrando os resultados
print("\n=== Resultados finais ===")
for aluno in alunos:
    print(f"aluno: {aluno['nome']} media: {aluno['media']:.2f} Situação {aluno['situacao']}")