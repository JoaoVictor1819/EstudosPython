# Menu em phyton

# Calculo de preço e desconto
def calcular_preco(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return desconto, preco_final

# Função para mostra detalhes do produto
def mostra_resumo(nome, preco, desconto, preco_final,):
    print("\n=== Descrição do produto ===")
    print(f"\nNome do produto: {nome}")
    print(f"Preço do produto: {round(preco)}")
    print(f"Desconto: {desconto}")
    print(f"Preço final {preco_final}")
    print("============================")

produtos = []

while True:
    print("1- Cadastrar produto")
    print("2- Lista de Produtos")
    print("3- Sair")
    

    opcao = input("Escolha uma das opções:")

    if opcao == '1':
        nome = input("Digite o nome do produto:")
        preco = float(input("Digite o preço do produto:"))
        tem_cupom = input("Digite sé tem cumpom: {s/n}")
        if tem_cupom == 's':
            percentual = float(input("Digite o percentual do desconto (%):"))
            desconto, preco_final = calcular_preco(preco, percentual)
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
        mostra_resumo(nome, preco, desconto, preco_final)

    elif opcao == '2':
        for produto in produtos:
            print(f"Nome: {produto['nome']}, Preço: {produto['preco']:.2f}, Desconto: {produto['desconto']}, Preço Final: {produto['preco_final']:.2f}")
    elif opcao == '3':
        print("Encerrando sistema. Ate a proxima")
        break
    else:
        print("Opção invalida. Tente novamente.")
    