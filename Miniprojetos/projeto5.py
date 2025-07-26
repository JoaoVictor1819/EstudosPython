# Desafio

# Sistema de cadastro de produtos com funções

# Função para classificar o produto
def classificar_preco(preco):
    if preco >= 100:
        return "Caro"
    elif preco >= 50:
        return "Preço Medio"
    else:
        return "Barato"
    
# Função para cadastrar um produto
def cadastrar_produto(produto):
    nome = input("Digite o nome do produto:")
    preco = float(input("Digite o preço do produto: R$"))

    classificacao = classificar_preco(preco)

    produto = {
        "nome": nome,
        "preco": preco,
        "classificacao": classificacao
    }

    return produto

# Lista para armazenar os produtos
produtos = []

# Loop principal para adicionar produtos
while True:
    produto = cadastrar_produto('produto')
    produtos.append(produto)

    continuar = input("Deseja cadastra mais algum produto? {s/n}")
    if continuar != 's':
        break

# Exibindo o Relatório final
print("\n=== Relatorio dos produtos ===")
for produto in produtos:
    print(f"\nNome: {produto['nome']}")
    print(f"Preço: R${produto['preco']:.2f}")
    print(f"Classificação: {produto['classificacao']}")