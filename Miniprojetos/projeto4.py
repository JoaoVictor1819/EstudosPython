# Desafio

# Sistema de Cadastro e Boletim de alunos com funções

# Função para caulcular a media

def media_calcular(n1, n2, n3):
    return (n1 + n2 + n3) / 3

# Função para determinar a situação com base na média
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
def cadastro_aluno():
    nome = input("Digite o nome do aluno(a):")
    idade = int(input("Digite a idade do aluno(a):"))
    nota1 = float(input("Digita a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))
    nota3 = float(input("Digite a terceira nota:"))

    media = media_calcular(nota1, nota2, nota3)
    situacao = verificar_situacao(media)

    aluno = { 
        "nome": nome,
        "idade": idade,
        "notas": [nota1, nota2, nota3],
        "media": media,
        "situacao": situacao
    }
    
    return aluno

# Lista para guardar os alunos

alunos = []

# Loop para cadastrar varios alunos

while True:
    aluno = cadastro_aluno()
    alunos.append(aluno)

    continuar = input("Deseja cadastrar outro aluno? (s/n)").lower()
    if continuar != 's':
        break

# Mostrando os Resultados
print("\n=== Boletim Final ===")
for aluno in alunos:
    print(f"\nNome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Media: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")
