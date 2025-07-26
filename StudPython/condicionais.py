# Condições em (if, elif, else)

# if condição:
    # Código se for verdadeiro
# elif outra_condição:
    # Código se a outra condição for verdadira
#else:
    # Código se nunhuma das condições for verdadeira


nota = float(input("Digite a nota do aluno(a):"))


if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")


# Desafio simples para pratica

idade = int(input("Digite sua idade:"))

if idade >= 18:
    print("Maior de idade")
elif idade >= 15:
    print("Adolescente")
else:
    print("Criança")


# Desafio 1

# Sistema de verificação de ingresso

idade = int(input("Digite a idade da pessoa:"))

if idade >= 60:
    print("Entrada gratuita para idoso")
elif idade >= 18:
    print("20 Reais (Adulto)")
elif idade >= 13:
    print("15 Reais (Adolecente)")
else:
    print("10 Reais (criaça)")


# Desafio 2

# Sistema de desconto de loja

produtos = [150.00, 50.70, 340.00]

total = sum(produtos)

print(f"Total sem desconto: R${total:.2f}")

forma_de_pagamento = input("Forma de pagamento (dinhero, pix, debito, credito):").lower

if forma_de_pagamento == "dinhero" or forma_de_pagamento == "pix":
    desconto = total * 0.10
elif forma_de_pagamento == "Debito":
    desconto = total * 0.05
else:
    desconto = 0.0

total_final = total - desconto

print(f"Desconto aplicado: R${desconto:.2f}")
print(f"Total a pagra: R${total_final:.2f}")




# Desafio 3

# Cadastro de alunos com requisitos de idade e nota 


nome = input("Digite aqui o nome do aluno(a):")
idade = int(input("Digite aqui a idade do aluno(a):"))

notas = [] # lista para armazenar 3 notas

for i in range(3):
    nota = float(input(f"Digite a nota {i+1}:"))
    notas.append(nota)

media = sum(notas) // len(notas)

print(f"\nAluno: {nome}")
print(f"\nidade: {idade}")
print(f"\nmedia: {media}")

# verifique se os alunos podem se escrever
if idade >= 15 and idade <=30 and media >=7:
    print("Aprovado")
else:
    print("Não foi aprovado")
