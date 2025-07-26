# Mini projeto

# Criando menus com opção while

# Menu de Cadastro de produtos

produtos = []

def cadastrar_produto():
    nome = input("Digite o nome do produto:")
    preco = float(input("Digite o preço do produto:"))
    produto = {
        "nome": nome,
        "preco": preco
    }
    produtos.append(produto)
    print("Produto cadastro com sucesso!")

    #função para lista de produtos
def lista_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\n=== Lista de Produtos ===")
        for i, produto in enumerate(produtos):
            print(f"{i+1}. Nome: {produto['nome']} Preço: R${produto['preco']:.2f}")

#função principal com o menu
def menu():
    while True:
        print("=== Menu ===")
        print("1- Cadastrar Produtos")
        print("2- Listar de Produtos")
        print("3- Sair")

        opcao = input("Escolha uma opção:")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            lista_produtos()
        elif opcao == '3':
            print("Encerrando programa")
            break
        else:
            print("Opção invalida. Tente novamente.")

 # Iniciar o programa
menu()