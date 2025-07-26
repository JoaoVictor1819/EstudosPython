# Mini Projeto com Menu

# Cadastro de Nomes Simples

nomes = []

# Função para adicionar um nome
def adicionar_nome():
    nome = input("Digite o nome para adicionar:")
    nomes.append(nome)
    print("Nome cadastrado com sucesso")


# Função para listar os nomes
def lista_nome():
    if len(nomes) == 0:
        print("Nenhum nome cadastrado.")
    else:
        print("\n=== Lista de Nome ===")
        for nome in nomes:
            print(f"- {nome}")

#Função com menu principal
def menu():
    while True:
        print("=== Menu ===")
        print("1- Adicionar Nome")
        print("2- Lista de Nome")
        print("3- Sair")

        opcao = input("Escolha uma opção:")

        if opcao == '1':
            adicionar_nome()
        elif opcao == '2':
            lista_nome()
        elif opcao == '3':
            print("Saindo do Programa")
            break
        else:
            print("Opção envalida. Tente novamente")


menu()
