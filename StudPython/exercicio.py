# Desafio 

# Cadastro de clientes de loja Fitness

# Lista para guardar os dados dos clientes
clientes = []

for i in range(3):
    print(f"\nCadastro do cliente {i+1}")
    nome = input("Digite o nome do cliente:")
    idade = int(input("Digite a idade do cliente:"))
    altura = float(input("Digite a altura do cliente:"))
    peso = float(input("Digite aqui o peso (Kg) do cliente:"))

    imc = peso / (altura**2)

    if imc <= 18.5:
        condicao = "Abaixo do peso"
    elif imc <= 24.9:
        condicao = "peso normal"
    elif imc <= 29.9:
        condicao = "sobrepeso"
    else:
        condicao = "Obesidade"

    if 18 <= idade <= 60 and 18.5 <= imc <= 29.9:
        promocao = "SIM"
    else:
        promocao = "NÃO"

    cliente = {
        "nome": nome,
        "idade": idade,
        "altura": altura,
        "peso": peso,
        "imc": round(imc, 2),
        "condicao": condicao,
        "promocao": promocao
    }

    clientes.append(cliente)

print("\n=== Relatorio final ===")
for c in clientes:
    print(f"\nCliente : {c['nome']}")
    print(f"Idade: {c['idade']} anos")
    print(f"Peso: {c['peso']}Kg")
    print(f"Altura: {c['altura']}m")
    print(f"IMC: {c['imc']}")
    print(f"Condição: {c['condicao']}")
    print(f"Promoção: {c['promocao']}")
