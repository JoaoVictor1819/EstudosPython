# O que é o "while"

contador = 1
    # Inicia a variavel com valor = 1

while contador <= 5: # enquanto o valor de contador for menor ou igual a 5, o bloco dentro será executado.
    print(f"contador: { contador}") # Mostra o valor atual
    contador += 1 # Adiciona 1 ao contador. Se você esquecer essa linha, o while vira um loop infinito.

    # Diferença entre for e while:

    # for 
    # Ideal quando você sabe quantas vezes repetir
    # usa range() ou lista
    # Exemplo: repetir 3 vezes

    #while
    # Ideal quando você não saber quantas vazes repetir
    # Usa uma condição lógica
    # Exemplo repetir ate o usuário digitar sair


resposta = ""

while resposta != "sair":
    resposta = input("Digite algo (ou 'sair' para parar:)")
    print(f"Você digitou: {resposta}")