#Mini progeto

# Recapitulando memorias

# Entrada, Saida e variaveis
nome = input("Digite o seu nome:")
idade =  int(input("Digite sua idade"))
print(f"Bem-Vindo  {nome}, Você  tem {idade} anos.")

# Condicionais (if, elif, else)
if idade >= 18:
    print("Maio de idade.")
else:
    print("Menor de idade.")

# Laços de repetição (while e for)
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

# Lista e dicionários
nomes = ["ana", "joao", "pedro"]
for nome in nomes:
    print(nome)

cliente = {"nome": "joao", "idade": 20}
print(cliente["nome"])

# Função com def
def saudacao(nome):
    print(f"Olá, {nome}")

saudacao("João")

# Parametro de retorno
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print("Resultado", resultado)

# Formatar números(Ex: evitar casas decimais)
preco = 19.8975
print(f"Preço formatado: R${preco:.2f}")

# Criar menu com while
while True:
    print("1- Ver mensagem\2 - Sair")
    opcao = input("Escolha:")
    if opcao == "1":
        print("Você esclheu ver a mensagem!")
    elif opcao == "2":
        break


# Mini sistema de Cadastro e login
usuarios = {}

def cadastrar():
    nome = input("Digite seu nome:")
    if nome in usuarios:
        print("usuário já existe.")
    else:
        senha = input("senha:")
        usuarios[nome] = senha

def login():
    nome = input("Nome de Usuário:")
    senha = input("Senha:")
    if usuarios.get(nome) == senha:
        print("login bem-sucedido")
    else:
        print("Usuário ou senha incorretos.")

