# Mini projeto com menu

produtos = [] # Lista onde entrarão os produtos

def cadastrar_produto():
    nome = input("Digite o nome do produto:")
    preco = float(input("Preço do produto (R$):"))

    tem_desconto = input("Tem cupom de desconto {s/n}:")
    if tem_desconto == "s":
        percentual = float(input("Digite o percentual de desconto (%): "))
        # Aqui você deve calcular o desconto e o preço final formatado com 2 casa decimais
        desconto = preco * (percentual / 100)
        preco_final = preco - desconto
    else:
        desconto = 0
        preco_final = preco

    produto = {
        "nome": nome,
        "preco": preco,
        "desconto": desconto,
        "preco_final": preco_final
    }

    produtos.append(produto)
    print("\nProduto cadastrado com sucesso")

def mostra_produtos():
    if not produtos:
        print("Nenhum produto cadastrado")
    else:
        print("\n=== Lista de produtos === ")
        for p in produtos:
            print(f"Nome {p['nome']}")
            print(f"Preço: {p['preco']:.2f}")
            print(f"Desconto {p['desconto']:.2f}")
            print(f"Preco final {p['preco_final']:.2f}")
            print("" * 30)

def remover_produto():
    nome_remover = input("Digite o nome do produto que deseja remover:")
    encontrado = False

    for i, produto in enumerate(produtos):
        if produto['nome'].lower() == nome_remover.lower():
            del produtos[i]
            print(f"Produto '{nome_remover}' removido com sucesso")
            encontrado = True
            break
    if not encontrado: 
        print("Produto não encontrado.")



# Menu
while True:
    print("=== Menu ===")
    print("1- Cadastre um produto")
    print("2- Lista de produto")
    print("3- Remover produto")
    print("4- Sair")

    opcao = input("Escolha uma opção:")

    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        mostra_produtos()
    elif opcao == '3':
        remover_produto()
    elif opcao == '4':
        print("Fim do programa")
        break
    else:
        print("Opção invalida. Tente novamente.")