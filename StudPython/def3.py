# Desafio: Corrigir o Codigo do sistema de produtos.


def classificar_preco(preco):
    if preco >= 100:
        return "Caro"
    elif preco >= 50:
        return "Medio"
    else:
        return "Barato"
    
# Função para cadastro produto
def cadastrar_produto(produto):
    nome = input("Digite aqui o nome do produto:")
    preco = float(input("Digite o preco do produto:"))

    classificar = classificar_preco(preco)

    produto = { 
        "nome": nome,
        "preco": preco,
        "classificacao": classificar
    }

    return produto

produtos = []

while True:
    produto = cadastrar_produto('produto')
    produtos.append(produto)

    continuar = input("Adicionar outro produto? (s/n):")
    if continuar != 's':
        break

    print("=== Lista de produtos ===")
    for produto in produtos:
        print(f"\nNome: {produto['nome']}, Preço: {produto['preco']:.2f} Classificação: {produto['classificacao']}")

    # Salvando em arquivos
    with open("Produtos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("=== Lista de produtos ===")
        for produto in produtos:
            linha = f"Nome: {produto['nome']} Preço{produto['preco']:.2f} Classificação: {produto['classificacao']}"

    print("\n Os produtos foram salvos no arquivo 'produtos.txt com sucesso!")