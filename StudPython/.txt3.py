# Cadastrando produtos com validação e armazenamento .txt

def cadastrar_produto():
    nome = input("Digite o nome do produto:")
    
    # Validação de preço
    while True:
        try:
            preco = float(input("Digite o preço do produto (R$):"))
            if preco <= 0:
                print("O preço deve ser maior que 0.")
            else:
                break
        except ValueError:
            print("Digite um valor numérivo válido para o preço.")

     # Verifica se tem desconto
    tem_desconto = input("Tem desconto? {s/n}").lower()
    if tem_desconto != 's':
            while True:
                try:
                    percentual = float(input("Digite o precentual de desconto (%):"))
                    if 0 <= percentual <= 100:
                        break
                    else:
                        print("O desconto deve ser entre 0 e 100.")
                except ValueError:
                    print("Digite um numero válido para o desconto.")
            desconto = preco * (percentual / 100)
    else:
            desconto = 0

    preco_final = preco - desconto   

   # Gravar os dados em arquivos .txt
    with open("Produto.txt", "a", encoding="utf-8") as arquivo:
            linha = f"{nome},{preco:.2f},{desconto:.2f},{preco_final:.2f}\n"
            arquivo.write(linha)
            
            print("Produto cadastrado com sucesso!")

def listar_produto():
    try:
        with open("Produto.txt", "r", encoding="utf-8") as arquivo:
            produtos = arquivo.readlines()

            if not produtos:
                print("Nenhum produto cadastrado ainda.")
                return
            
            print("=== Lista de Produtos ===")
            for linha in produtos:
                nome, preco, desconto, preco_final = linha.strip().split(",")
                print(f"Nome: {nome}")
                print(f"Preço: R$ {preco}")
                print(f"Desconto: R$ {desconto}")
                print(f"Preço Final: R$ {preco_final}")
                print("-" * 30)
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum produto cadastrado ainda.")


while True:
    print("=== Menu ===")
    print("1- Cadastrar Produto")
    print("2- Listar de Produtos")
    print("3- sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        listar_produto()
    elif opcao == '3':
        print("Programa encerrado. ate a proxima!")
    else:
        print("Opção inválida. tente novamente.")