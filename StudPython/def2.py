# Função que calcula a média de 3 notas


def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

# Entrada de dados

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

# Chamando a função

media_total = calcular_media(nota1, nota2, nota3)

# Verifica a situação

if media_total >= 7:
    situacao = "Aprovado"
elif media_total >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"\nMedia final: {media_total:.2f}")
print(f"Situação do aluno: {situacao}")