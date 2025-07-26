# Aprendedendo a Criar sistema de login e cadastro de usuário.

usuasrios = []

def cadastrar():
    nome =input("Digite o Nome do Usuário:")
    senha = input("DIgite a Senhas de Usuário:")
    usuario = {"nome": nome, "senha": senha}
    usuasrios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def login():
    nome = input("Digite o nome do Usuário:")
    senha = input("Digite a Senha do Usuário:")
    for usuario in usuasrios:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            print("Login realizado com sucesso!")
            return
        print("Nome de Usuário ou senha incorretos.")

while True:
    print("=== Menu ===")
    print("1- Cadastrar-se")
    print("2- Login")
    print("Sair")

    opcao = input("Escolha uma das opções:")

    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        login()
    elif opcao == '3':
        print("Saindo do Sistema")
        break
    else:
        print("Opção invalida. tente novamente.")