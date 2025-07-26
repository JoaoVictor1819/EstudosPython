# Projeto: Sistema de cadastro com salvamento Automático

print("=== Sistema de Cadastro de Alunos com Salvamento ===")
alunos = []

while True:
    nome = input("Digite o nome do Aluno(a):")
    idade = int(input("Digite a idade do Aluno(a):"))
    

    notas = []
    for i in range(3):
        nota = float(input(f"Digite a nota {i+1}:"))
    notas.append(nota)

    media = sum(notas) / len(notas)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    aluno = {
        "nome": nome,
        "idade": idade,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)


    # Salvar os arquivos
    with open("alunos.txt", "a", encoding="utf-8") as arquirvos:
        arquirvos.write(f"Nome: {nome}, idade: {idade}, Notas: {notas}, Média: {media}, Situação: {situacao}")
    
    continuar = input("\nDeseja cadastra outro aluno? (s/n:)").lower()
    if continuar != "s":
        break

    # Exibir todos no final
print("\n=== Resultado Final ===")
for aluno in alunos:
    print(f"\nNome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Media: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")