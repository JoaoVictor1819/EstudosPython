# parâmetro e retorno de valores em python

# def somar(a, b):
#    resultado = a + b
#    return resultado

# print(somar(3, 4)) # vai imprimir 7

# Função que recebe dois números e retorna a soma
def somar(a, b):
    resultado = a + b  # Soma os dois valores
    return resultado   # devolve a soma para quem chamou a função

# Chamando a função e armazenando o resultado
soma = somar(5, 10)

print(f"A soma é: {soma}")