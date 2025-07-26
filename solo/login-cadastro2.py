# Login cadastro

# Cadastro

usuario = {}

def cadastrar_usuarios():
    nome = input("Digite o nome de Usuário:")
    if nome in usuario:
        print("Usuário já existente. tente novamente.")
    else:
        senha = input("Digite a senha do usuário:")
        usuario[nome] = senha
        print("Usuário cadastrado com sucesso.")

# Login de usuário

def login_usuario():
    print("== login de Usuário ==")

    tentativas = 3

    while tentativas > 0:
        nome = input("Digite o nome de Usuário:")
        senha = input("Senha:")

        if nome in usuario and usuario[nome] == senha:
            print(f"Login realizado com suceso! Bem vindo {nome}")
        else:
            tentativas -= 1
            print(f"Dados incorretos. tentarivas {tentativas}")

    print("Número de tentativas excedido. Acesso bloqueado")

# Menu 

while True:
    print("== Menu ==")
    print("1- Cadastro de Usuário")
    print("2- Login")
    print("3- Sair")

    opcao = input("Escolha uma das opções:")


    if opcao == "1":
        cadastrar_usuarios()
    elif opcao == "2":
        login_usuario()
    elif opcao == "3":
        print("Programa encerrado. Tchau")
        break
    else:
        print("Opção ivalida. tente novamente")