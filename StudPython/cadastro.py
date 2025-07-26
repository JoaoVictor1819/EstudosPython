import json
import os
# Tenta carregar dados já salvos
if os.path.exists("pessoas.json"):
    with open("pessoas.json", "r", encoding="utf-8") as arquivo: pessoas = json.load(arquivo)
else:
    pessoas = {}
def salvar_dados():
    with open("pessoas.json", "w", encoding="utf-8") as arquivo:
        json.dump(pessoas, arquivo, ensure_ascii=False, indent=4)
# Sistema de Cadastro de Pessoas feito em modelo de dicionário
# Este sistema permite cadastrar pessoas com nome, idade e altura,
pessoas = {
    "João": {"idade": 18, "altura": 1.75},
    "Maria": {"idade": 20, "altura": 1.65},
    "Pedro": {"idade": 22, "altura": 1.80}
}
print("Bem-vindo ao sistema de cadastro de pessoas!")

# Função para exibir todas as pessoas cadastradas

def mostrar_pessoas():
    print("\n--- Lista de Pessoas Cadastradas --- ")
    for nome, info in pessoas.items():
        print(f"Nome: {nome}, idade: {info['idade']}, altura:{info['altura']}")

# Função para adicionar uma nova pessoa

def adicionar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    altura = float(input("Digite a altura da pessoa (em metros): "))
    pessoas[nome] = {"idade": idade, "altura": altura}
    print(f"{nome} foi adicionado com sucesso!")

# loop principal do sistema
while True:
    print("\nMenu:")
    print("1. Mostrar pessoas cadastradas")
    print("2. Adicionar nova pessoa")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        mostrar_pessoas()
    elif opcao == "2":
        adicionar_pessoa()
    elif opcao == "3":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")   
   