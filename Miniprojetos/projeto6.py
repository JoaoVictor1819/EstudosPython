# Mini projeto

# Sistema de Cadastro de Clientes de Academia

# Função para calcular IMC e classificar
def calcular_imc(peso, altura):
    imc = round(peso / (altura**2), 2) # Formula do IMC
    if imc < 18.5:
        Classificacao = "Abaixo do peso"
    elif imc < 25:
        Classificacao = "Peso ideal"
    elif imc < 30:
        Classificacao = "Sobrepeso"
    else: 
        Classificacao = "Obesidade"

    return imc, Classificacao
    
    # Lista onde ficara os dados armazenados dos 
    #clientes
     
clientes = []

    # Início do loop para cadastrar vários clientes 
while True:
        print("\n=== Cadastro do cliente ===")
        nome = input("Digite o nome do cliente:")
        idade = int(input("Digite a idade:"))
        peso = float(input("Digite o peso (Kg):"))
        altura = float(input("Digite a altura (m):"))

        # Usando a função criada antes para calcular IMC e classificar
        imc, Classificacao = calcular_imc(peso, altura)

        cliente = {
            "nome": nome,
            "idade": idade,    
            "peso": peso,
            "altura": altura,
            "imc": round(imc, 2), # arredondando aqui
            "classificacao": Classificacao
        }

        # Adicionando o dicionario a lista vazia
        
        clientes.append(cliente)

        # Pergunta se o Usúario que continuar 
        continuar = input("Gostaria de cadastrar mais algum cliente: {s/n}")
        if continuar.lower() != 's':
            break

        print("\n=== Resultado Final ===")
        for cliente in clientes:
            print(f"\nNome: {cliente['nome']}")
            print(f"Idade: {cliente['idade']} anos")
            print(f"Peso: {cliente['peso']}Kg")
            print(f"Altura: {cliente['altura']}M")
            print(f"IMC: {cliente['imc']:.2f}")
            print(f"Classificação: {cliente['classificacao']}")
