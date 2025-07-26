# Mini projeto

# Sistema de controle de estoque de loja

produtos = []

while True:
    print("\n===  Menu da loja ===")
    print("1 - Cadastrar novo produto")
    print("2 - Lista de produtos")
    print("3 - Verificar disponibilidade")
    print("4 - Calcule valor total do estoque")
    print("5 - sair")


    opcao = input("Escolha uma opção:")

    if opcao == "1":
        nome = input("Nome do produto:")
        preco = float(input(" preco do produto:"))
        quantidade = int(input("quantidade em estoque:"))

        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade":quantidade
        }

        produtos.append(produto)
        print(f"{nome} Cadastrado com sucesso!")

    elif opcao == "2":
        print("\n=== Produtos Cadastrados ===")
        for p in produtos:
            print(f" - {p['nome']}  preço: R${p['preco']} Estoque: {p['quantidade']}")
    
    elif opcao == "3":
        buscar = input("Digite o nome do produto para buscar:")
        encontrado = False
        for p in produtos:
            if p["nome"].lower() == buscar.lower():
                if p["quantidade"] > 0:
                    print(f"{p['nome']} está disponivel! quantidade {p['quantidade']}")
                else:
                     print(f"{p['nome']} Produto fora de estoque!")
            if not encontrado:
                print("Produto não encontrado.")
    elif opcao == "4":
        total = 0 
        for p in produtos:
            total += p["preco"] * p["quantidade"]
        print(f"Valor total do estoque: R${total:.2f}")

    elif opcao == "5":
        print("Saida do Sistema... Ate logo")
        break

    else:
        print("Opção inválida. tente novamente")
    
    
    