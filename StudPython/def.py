# Funções com "def"

#def nome_da_funcao(parametro):
    # Bloco de codigo
  #  return algo # (opicional)



def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")


def somar(num1, num2):
    resultado = num1 + num2
    return resultado

# chamando a dunção e exibindo o resultado
valor1 = float(input("Digite o primeiro número:"))
valor2 = float(input("Digite o segundo número:"))

soma = somar(valor1, valor2)
print(f"A soma ente {valor1} e {valor2} é: {soma}")
    