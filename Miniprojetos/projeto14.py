# Lista de cadastro de produtos 

produtos = []
def cadastrar_produtos():
    nome = input("Digite o nome do produto:")
    preco = float(input("O preço:"))


    tem_desconto = input("O produto tem desconto? {s/n}")
    if tem_desconto == 's':
        precentual = float(input("Digite o percetual do desconto (%):"))# Aqui se deve calcular o desconto e o preço final formatando com 2 casas decimais
        desconto = preco * (precentual / 100)
        preco_final = preco - desconto

    else:
        desconto = 0
        preco_final = preco

    produto = {
        "nome": nome,
        "preco": preco,
        "desconto": desconto,
        "precofinal": preco_final
    }

    produtos.append(produto)
    print("\nProduto Cadastrado com sucesso")


def mostra_produto():
   if not produtos:
       print("Nenhum produto cadastrado")
   else:
       print("=== Lista de produto ===")
       for p in produtos:
        print(f"Nome: {p['nome']}")
        print(f"preco: {p['preco']:.2f}")
        print(f"Desconto {p['desconto']:.2f}")
        print(f"Preço Final: {p['precofinal']:.2f}")

def remover_produto():
   nome_remover = input("Digite o nome do produto que gostaria de remover:")
   encontrado = False

   for i, produto in enumerate(produtos):
      if produto['nome'].lower() == nome_remover.lower():
         del produto[i]
         print(f"produto '{produto} removido com sucesso.")
         encontrado = True
         break
      if not encontrado:
        print("Produto não encontrado.")

    # Menu

while True:
   print("Menu")
   print("1- Cadastrar produto")
   print("2- Mostra produtos cadastrados")
   print("3- Remover produto")
   print("4- Sair")

   opcao = input("Escolha uma opção:")

   if opcao == '1':
      cadastrar_produtos()
   elif opcao == '2':
      mostra_produto()
   elif opcao == '3':
      remover_produto()
   elif opcao == '4':
      print("Fim do programa. volte sempre.")
      break
   else:
      print("Opção envalida. tente novamente.")  