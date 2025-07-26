# Mini projeto com menu

# Sistema de Cadastro com idade e classificação

cadastros = []


def classificar_idade(idade):
    if idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolecente"
    else:
        return "Adulto"


def adicionar_cadastro():
    nome = input("Digite o nome da pessoa:")
    idade = int(input("Digite a idade:"))
    classificacao = classificar_idade(idade)

    pessoa = {
        "nome": nome,
        "idade": idade,
        "classificacao": classificacao
    }
    cadastros.append(pessoa)
    print("Pesso Cadastrada com sucesso!")

def lista():
    if not cadastros:
        print("Nenhuma pessoa cadastrada.")
    else:
        print("\n=== Lista de pessoas cadastrada ===")
        for pessoa in cadastros:
            print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Classificação: {pessoa['classificacao']}")

def menu():
    while True:
        print("Menu")
        print("1- Cadastrar pessoa")
        print("2- Lista de pessoa")
        print("3- Sair")

        opcao = input("Escolha uma das opções:")

        if opcao == '1':
            adicionar_cadastro()
        elif opcao == '2':
            lista()
        elif opcao == '3':
            print("Você saio do programa")
            break
        else:
            print("Opção invalidade. Tente novamente")

# Iniciar o Programa
menu()