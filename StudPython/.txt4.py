# Menu de login com cadastro de produtos

usuarios = {} # Dicionário para guardar usuários (nome: senha)

produtos = [] # Lista para guardar produtos em memória

# Função para cadastrar novo usuário
def cadastrar_usuario():
    nome = input("Digite o nome de usuário:")
    if nome in usuarios:
        print("Usuário já existe. tente outro nome.")
    else:
        senha = input("Digite a senha:")
        usuarios[nome] = senha
        print("Usuário cadastrado com sucesso!")

# Função para fazer login
def login():
    print("\n=== Login ===")
    tentativas = 3
    while tentativas > 0:
        nome = input("Nome de usuário:")
        senha = input("Senha:")
        if nome in usuarios and usuarios[nome] == senha:
            print(f"Login realizado com sucesso! Bem-vendo, {nome}!")
            return True
        else:
            tentativas -= 1
            print(f"Dados incorretos. Tentativas restantes: {tentativas}")
    print("Número máximo de tentativas excedido. Acesso bloquado.")
    return False

# Função para cadastrar produto
def cadastrar_produto():
    nome = input("Digite o nome do produto:")


    while True:
        try:
            preco = float(input("Digite o proço do produto (R$):"))
            if preco <= 0:
                print("O preço deve ser maior que 0.")
            else:
                break
        except ValueError:
            print("Valor inválido. Por favor, digite um número valaido para o preço")

    tem_desconto = input("Tem desconto? (s/n):").lower()
    if tem_desconto == 's':
       while True:
           try:
               percentual = float(input("Digite o precentual de desconto (%):"))
               if 0 <= percentual <= 100:
                   break
               else: 
                   print("O desconto deve ser entre 0 e 100.")
           except ValueError:
               print("Digite um número válido para o perecentual de desconto.")
       desconto = preco * (percentual / 100)
    else:
        desconto = 0

    preco_final = preco - desconto

    with open("produtos.txt", "a", encoding="utf-8") as arquivo:
            linha = f"{nome}, {preco:.2f}, {desconto:.2f}, {preco_final:.2f}\n"
            arquivo.write(linha)
    print("Produto cadastrado com sucesso!")  

# Dunção para listar os produtos
def listar_produtos():
    try:
        with open("produtos.txt", "r", encoding="utf-8") as arquivo:
            produtos = arquivo.readlines()

            if not produtos:
                print("Nenhum produto cadastrado.")
                return

            print("\n=== Lista de Produtos ===")
            for linha in produtos:
                partes = linha.strip().split(",")

                if len(partes) != 4:
                    print("Linha inválida no arquivo, palando...")
                    continue

                nome, preco, desconto, preco_final = linha.strip().split(",")
                print(f"Nome: {nome}")
                print(f"Preço: R$ {preco}")
                print(f"Desconto: R$ {desconto}")
                print(f"Preço Final: R$ {preco_final}")   
                print("-" * 30) 
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum produto cadastrado.")

# Menu inicial: Cadastro e Login


while True:
    print("\n=== Sistema de Acesso ===")
    print("1- Cadastrar novo usuário")
    print("2- Fazer login")
    print("3- Sair")
    escolha = input("Escolha uma opção:")

    if escolha == '1':
        cadastrar_usuario()
    elif escolha == '2':
        if login():
            # Menu de produtos so aparece se o login for finalizado corretamente
            while True:
                print("\n=== Menu de Produtos ===")
                print("1- Cadastrar um  produto")
                print("2- Listar produtos")
                print("3- Sair do sistema")
                opcao = input("Escolha um opção:")

                if opcao == '1':
                    cadastrar_produto()
                elif opcao == '2': 
                    listar_produtos()
                elif opcao == '3':
                    print("Saindo do sistema...")
                    break
                else:
                    print("Opção invalida. Tente novamente")
    elif escolha == '3':
        print("Finalizando o programa...")
        break
    else: 
        print("Opção ivalidade. tente novamente.")