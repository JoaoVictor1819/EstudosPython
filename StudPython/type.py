# type()

#x = 1.5
#print(type(x)) # <class 'float'>

#x = 5
#print(type(x)) # <class 'int'>

# text "type()"

nome = "João"
idade = 18
altura = 1.73
eh_maior = True
lista = [1, 2, 3]
dicionario = {"chave": "valor"}

print(type(nome)) # <class 'str'> texto(string)
print(type(idade)) # <class 'int'> Numero inteiro
print(type(eh_maior)) # <class 'bool'>  Booleano (True ou False)
print(type(altura)) # <class 'float> Numero com ponto (float)
print(type(lista)) # <class 'list> Lista
print(type(dicionario)) # <class 'dict'> Dicionário

# Para que serve o type() na prática?
# Você usa type() para:
# Verificar o tipo de um valor que o usuário digitou
# entender o que uma variável esta armazenando
# Ajudar a resolver erros de código
# Verificar o tipo de uma variável antes de fazer operações com ela

# Desafio pra praticar:
# crie um progrma simples que:
# 1. Pergunte o nome, idade, altura da pessoa
# 2. Mostra o tipo de cada resposta

nome = input("Digite seu nome:")
idade = int(input("Digite dua idade:"))
altura = float(input("Digite sua altura:"))

print("\n menu de tipos")
print("nome:", type(nome)) # <class 'str'>
print("idade:", type(idade)) # <class 'int'>
print ("altura:", type(altura)) # <class 'float'>

# Dica: use o input() para receber dados do usuário

idade = 10
print(type(idade)) # <class 'int'> Numero inteiro

altura = 1.75
print(type(altura)) # <class 'float'> Numero com ponto (float)

texto = "Olá, mundo!"
print(type(texto)) # <class 'str'> texto(string)

maior = True
print(type(maior)) # <class 'bool'>  Booleano(True ou False)

menor = False
print(type(menor)) # <class 'bool'>  Booleano (True ou False)

lista = [1500, 4500, 7300]
print(type(lista)) # <class 'list'> Lista

dicionario = {
    "joao" : {"idade": 18, "altura": 1.75},
    "Maria" : {"idade": 20, "altura" : 1.65},
} 
print(type(dicionario)) # <class 'dict'> Dicionário

idade = (input("digite sua idade:"))
print(type(idade)) # <class 'str'> texto(string)

idade = int(input("digite sua idade:"))
print(type(idade)) # <class 'int'> Numero inteiro

resultado = 10 / 2
print(type(resultado)) # <class 'float'> Numero com ponto (float)

soma = 5 + 3
print(type(soma)) # <class 'int'> Numero inteiro

