# Desafio 

# Avaliação para plano de academia

# Entrada de dados
nome = input("Digite o nome do cliente:")
idade = int(input("Digite a idade do cliente:"))
peso = float(input("Digite o peso (Kg):"))
altura = float(input("Digite a altura (m):"))

# Verificado tipos (só para treinar)
print("\n--- tipos de dados ---")
print("nome", type(nome))
print("idade", type(idade))
print("peso", type(peso))
print("altura", type(altura))

# Cálculo do IMC
imc = peso / (altura**2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc <= 24.9:
    classificacao = "Peso normal"
elif imc <= 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

# Exibe os dados do cliente
print("\n--- Resultado ---")
print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"imc: {imc}")
print(f"classificacao: {classificacao}")

# Verifique se pode se inscrever
if idade >= 16 and idade <= 60 and imc >= 18.5 and imc <= 29.9:
    print("Pode se inscrever no plano da academia.")
else:
    print("Não pode se inscrever no plano da academia")