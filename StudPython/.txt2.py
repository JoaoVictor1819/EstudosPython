# Aprendendo a usar arquivo .txt com Python

def cadastrar_usuario():
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade:"))

    with open("usuario.txt", "a") as arquivo:
        arquivo.write(f"{nome},{idade}\n")

        print("Usuario cadastrado com sucesso!")

def lista_usuario():
    try:
        with open("usuario.txt", "r") as arquivo:
            linhas = arquivo.readlines()

            if not linhas:
                print("Nenhum usuário cadastrado ainda.")
                return
            
            print("=== Lista de Usuários cadastrados ===")
            for linha in linhas:
                nome, idade = linha .strip().split(",")
                print(f"Nome: {nome}, Idade: {idade}")
    except FileExistsError:
        print("Arquivo não encontrado. Nenhum usuário cadastrado ainda.")


# Menu principal

while True:
    print("=== Menu ===")
    print("1- Cadastrar Usuário")
    print("2- Listar de Usuários")
    print("3- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        lista_usuario()
    elif opcao == '3':
        print("Fim do programa. Ate a proxima!")
    else:
        print("Opção inválida. Tente novamente.")