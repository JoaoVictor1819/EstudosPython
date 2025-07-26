# Menu em python



def calcular_preco(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return desconto, preco_final

def mostra_resumo(nome, preco, desconto, preco_final):
    print("\n=== Resumo da Compra ===")
    print(f"Produto: {nome}")
    print(f"Preço original: R$ {preco:.2f}")
    print(f"Desconto: {desconto:.2f}")
    print(f"Preço com desconto: R${preco_final:.2f}")
    print("==============================")

# Lista onde serão armazenados os dados
produtos = []


while True:
    print("\n=== Menu ===")
    print("1- Cadastrar produto")
    print("2- Produtos Cadastrados")
    print("3- Sair")

    opcao = input("Escolha uma opção:")

    if opcao == '1':
        nome = input("Digite o nome do produto:")
        preco = float(input("Digite o preço do produto:"))
        tem_cupom = input("Digite se tem cupom: {s/n}:")
        if tem_cupom.lower() == 's':
            precentual = float(input("Digite o percentual do desconto (%):"))
            desconto, preco_final = calcular_preco(preco, precentual)
        else:
            desconto = 0
            preci_final = preco

            produto = {
                "nome": nome,
                "preco": preco,
                "desconto": desconto,
                "preco_final": preci_final            
            }

            produtos.append(produto)
            mostra_resumo(nome, preco, desconto, preco_final)

    elif opcao == '2':
        print("\n=== Lista de Produtos ===")
        for produto in produtos:
            mostra_resumo(produto[nome], produto[preco], produto[desconto], produto[preco_final])
    
    elif opcao == '3':
        print("Encerrando sistema. Ate a proxima!")
        break


    else: 
        print("Opção invalida. tente novamente.")




