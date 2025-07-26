# Treino de python  tela de cadastro

# Cadastro simples de usuario

usuarios = {}

def cadastro_usuario():
    nome = input("Digite o nome de Usuário:")
    if nome in usuarios:
        print("Usuário ja existe. tente outro nome.")
    else:
        senha = input("Digite a senha:")
        usuarios[nome] = senha
        print("Usuário cadastrado com sucesso!")


# Sistema de login
def login_usuario():
    print("=== Login de Usuário ===")

    tentativa = 3

    while tentativa > 0:
        nome = input("Nome de Usuário:")
        senha = input("Senha:")

        if nome in usuarios and usuarios[nome] == senha:
         print(f"Login realizado com sucesso! Bem vindo, {nome}")
        else:
         tentativa -= 1
        print(f"Dados incorretos. Tentativas restantes:{tentativa}")

print("Número de tentava exedido. Acesso bloqueado")
  
  #Integra menu a cadastro e login

while True:
    print("=== Menu ===")
    print("1- Cadastre-se")
    print("2- Logar")
    print("3- sair")

    opcao = input("Escolha das opções:")

    if opcao == "1":
        cadastro_usuario()
    elif opcao == "2":
        login_usuario()
    elif opcao == "3":
        print("Sistema incerrado. Tchau")
        break
    else:
        print("Opção envalida. tente novamente")