# Validação de dados

def validadeidade():
    while True:
        try:
            idade = int(input("Digite sua idade:"))
            if idade >= 0:
                return idade
            else:
                print("Idade não pode ser negativa.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")


def validarsenha():
    while True:
        senha = input("Digite sua senha (Minimo 6 caracteres):")
        if len(senha) >= 6:
            return senha
        else:
            print("Seha muito curta. tente novamente.")

usuarios = {}

def cadastrausuario():
    nome = input("Digite o nome de usuario:")
    if nome in usuarios:
        print("Usuario cadastrado com sucesso")
    else:
        idade = validadeidade()
        senha = validarsenha()
        usuarios[nome] = {"idade": idade, "senha": senha}
        print("Usuário cadastrado com sucesso.")

# Sistema de menu

while True:
    print("=== Menu ===")
    print("1- Cadastre-se")
    print("2- Sair")

    opcao = input("Escolha a opção:")

    if opcao == '1':
        cadastrausuario()
    elif opcao == '2':
        print("fim do programa. tchau")
    else:
        print("Opção ivalida. tente novamente.")