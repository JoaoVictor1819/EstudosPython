## Operadores Aritméticos em Python
# + adição 2 + 3 = 5
# - subtração 5 - 2 = 3
# * multiplicação 2 * 3 = 6
# / divisão 10 / 2 = 5.0
# // divisão inteira 10 // 3 = 3
# % Resto de divisão 10 % 3 = 1
# ** potência 2 ** 3 = 8

a = 10
b = 3

print(a + b) # soma 13
print(a - b) # subtração 7
print(a * b) # multiplicação 30
print(a / b) # divisão 3.3333333333333335
print(a // b) # divisão inteira 3
print(a % b) # resto da divisão 1
print(a ** b) # potência 1000

# Operadores Relacionais (Comparam valores e retornam booleanos como true ou false)

# == igual 5 == 5 = True
# != diferente 5 != 3 = True
# > maior 7 > 4 = True
# < menor 3 < 8 = True
# >= maior ou igual 5 >= 5 = True
# <= menor ou igual 2 <= 1 = False

idade = 18
print(idade == 18) # true (é igual)
print(idade != 17) # true (é diferente)
print(idade > 16)  # true (é maior)
print(idade < 20)  # true (é menor)
print(idade >= 18) # true (é maior ou igual)
print(idade <= 18) # true (é menor ou igual)

# Operadores Lógicos (ligam comparações e retornam booleanos)

# Operadores/ Nome/ Explicação/
# and   E    Verdadeiro se as duas condições forem verdadeiras
# or    OU   Verdadeiro se pelo menos uma condição for verdadeira
# not   NÃO  Inverte o valor lógico da condição(True para False e vice-versa)

idade = 20
altura = 1.75

# and: as duas precisam ser verdadeiras
print(idade > 18 and altura > 1.70) # True (idade é maior que 18 e altura é maior que 1.70)

print(idade < 18 or altura > 1.70) # True (idade é menor que 18 ou altura é maior que 1.70)

print(not idade < 18) # True (idade é maior ou igual a 18, então not inverte para True)

# Desafio

a = 4
b = 2
c = 6

print(a + b * c) # (4 + 2 * 6) = 4 + 12 = 16, pois a multiplicação tem precedência sobre a adição



print((a + b) * c)  # (4 + 2) * 6 = 6 * 6 = 36, pois os parênteses têm precedência sobre a multiplicação


print(a > b and c > a) # (true. pois as duas condições são verdadeiras)


print( a == 4 or b == 5) # (true. pois pelo menos uma é verdadeira)


print(not a ==3) # (true. pois a não é igual a 3, então not inverte para True)

# Arquivo interativo para testar operadores

# Mostra titulo para o usuário
print("== Prática com Operadores em Python ==")

# Pergunta ao usuário um número E converte para inteiro
a = int(input("Digite um número inteiro (a):"))
b = int(input("Digite um numero inteiro (b):"))

# Realizendo operações aritméticas
print(f"\n Operações com {a} e {b}:")
print(f"Soma {a} + {b} = {a + b}")  
print(f"Subtração {a} - {b} = {a - b}")
print(f"Multiplicação {a} * {b} = {a * b}")
print(f"Divisão {a} / {b} = {a / b}")
print(f"Divisão inteira {a} // {b} = {a // b}")
print(f"Resto da divisão {a} % {b} = {a % b}")
print(f"Potência {a} ** {b} = {a ** b}")

# Relacionais
print(f"\n Comparações entre {a} e {b}:")
print(f" {a} == {b} é {a == b}")
print(f" {a} != {b} é {a != b}")
print(f" {a} > {b} é {a > b}")
print(f" {a} < {b} é {a < b}")
print(f" {a} >= {b} é {a >= b}")
print(f" {a} <= {b} é {a <= b}")

# Lógicos
print(f"\n Operadores lógicos com {a} e {b}:")
print(f"({a} > 5) and ({b} > 5) é {(a > 5) and (b > 5)}")
print(f"({a} < 10) or ({b} < 10) é {(a < 10) or {b <10}}")
print(f"not ({a} == {b}) é {not (a == b)}")



#========================================



# Desafio final

print(" === Sistema de pedidos da lanchonete ===")

# Entrada dos valores dos itens
lanches = float(input("Digite o valor do lanche: R$ "))
bebidas = float(input("Digite o valor da bebida: R$ "))
sobremesa = float(input("Digite o valor da sobremesa: R$ "))

# Cálculo do total
total = lanches + bebidas + sobremesa
print(f"\n Total do pedido: R$ {total:.2f}")

# Classifivicação do pedido
if total < 20:
    print("pedido pequeno")
elif total < 50:
    print("pedido médio")
else:
    print("pedido grande")

# Verificando os benefícios
if total > 60:
    print("Você ganhou um brinde!")
elif total > 40 and total <= 60:
    print("Cliente ganhou um desconto de 10%!")
else:
    print("Obrigado pelo pedido!")


#=====================================

# Desafio 2

# Sistema  simples onde o cliente digita 3 notas de um aluno, ele calcula a média e me diz
# "Se o aluno foi aprovado (média maior ou igual a 7)"
# "Recuperação (média entre 5 6.9)"
# "Ou reprovado (média menor que 5)"

print("=== Sistema de avalição de alunos ===")

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

# Entradas de notas
media = (nota1 + nota2  + nota3) / 3
print(f"\n Média final: {media:.2f}")

# Verifique os resultados 
if media >= 7:
    print("Aluno aprovado.")
elif media >= 5:
    print("Aluno de recuperação")
else:
    print("Aluno reprovado")

#verifique se é destaque
if media > 9:
    print("Parabens aluno destaque")


#=============================

alunos = []

    # Exemplo de repetição para adicionar vários alunos
for i in range(3): #depois pode mudar para while e      deixar  ilimitado
    nome = input(f"\nDigite o nome {i+1} aluno:")

    nota1 = float(input("Digite a primeira nota:")) 
    nota2 = float(input("Digite a segunda nota:"))
    nota3 = float(input("Digite a terceira nota:"))

    media = (nota1 + nota2 + nota3) / 3

#verificar situação
if media >= 7:
    situacao = "aprovado"
elif media >= 5:
    situacao = "recuperação"
else:
    situacao = "reprovado"

# Criando dicionario para alunos
aluno = {
    "nome" : nome,
    "notas" : [nota1, nota2, nota3],
    "media": media,
    "situacao": situacao
}

# adicionando o dicionario a lista
alunos.append(aluno)

# Mostra todos os resultados 
print("\n=== Resultados finais ===")

for aluno in alunos:
    print(f"Aluno: {aluno['nome']} Media: {aluno['media']:.2f}  situacao: {aluno['situacao']}")

