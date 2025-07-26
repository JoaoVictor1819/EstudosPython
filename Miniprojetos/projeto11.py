# Mini projeto de login e cadastro de usuario

#Etapa 1 - Cadastro simples de Usuário

usuarios = {}  # Dicionario para armazenar os usuarios

def cadastrar_usuario():
    nome = input("Digite o nome do usuário:")
    if nome in usuarios:
        print("Usuário já existe. tente outro nome.")
    else:
        senha = input("Digite a senha de Usuário:")
        usuarios[nome] = senha
        print("Usuário Cadastrado com sucesso")


# Etapa 2 - Sistema de login
def login_usuario():
    print("\n=== Sistema de Login ===")

    tentativas = 3

    while tentativas > 0:
      nome = input("Nome de Usuário:")
      senha = input("Senha:")

      if nome in usuarios and usuarios[nome] == senha:
        print(f"Login relaizado com sucesso! Bem-vindo, {nome}")
      else:
        tentativas -= 1
        print(f"Dados incorretos. Tentativas restantes: {tentativas}")


print("Número de tentativas excedido. Acesso bloqueado")

# Etapa 3 - Integrar Menu: Cadastro de login


while True:
    print("=== Menu ===")
    print("1- Cadastro novo Usuáriop")
    print("2- Fazer Login")
    print("3- Sair")
    
    opcao = input("Escolha uma das opções aprensentadas:")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        login_usuario()
    elif opcao == "3":
        print("Sistema incerrado. Ate a proxima")   
    else:
        print("Comando invalido. tente novamente.")     