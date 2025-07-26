# Mini projeto

# Sistema de cadastro de Clientes para uma loja de Roupas

clientes = []

while True:
    print("\n=== Cadastro de Cliente ===")

    nome = input("\nNome do clinte:")
    idade = int(input("Idade do cliente:"))

    if idade < 18:
        print("Cliente menor de idade. Cadastro não permitido.")
    else:
        # Lista para guardar os 3 valores dos produtos
        compras = []

        # Loop para registrar 3 produtos

        for i in range(3):
            valor = float(input(f"Digite o valor do produto {i+1}: R$"))
            compras.append(valor)

         # Total da compra

            total = sum(compras)

        # Aplicar o desconto se o total dormais que R$ 300

        if total > 300:
            desconto = total* 0.1 #10%
            total_com_desconte = desconto
        else:
            desconto = 0
            total_com_desconte = total

        # Define o tipo do cliente com base no valor gasto

        if total_com_desconte > 500:
            situacao = "Cliente VIP"
        else:
            situacao = "Cliente comum"

        # Criando um dicionario


        cliente = {
            "nome": nome,
            "idade": idade,
            "compras": compras,
            "total": total,
            "desconto": desconto,
            "final": total_com_desconte,
            "situacao": situacao
        }
        clientes.append(cliente)

        continuar = input("\nDeseja cadastrar outro cliente? (s/n):").lower()
        if continuar != 's':
            break

        # Exibir o relatorio final
        print("\n=== Relatorio do Cliente ===")
        for c in clientes:
            print(f"\nNome: {c['nome']}")
            print(f"Idade: {c['idade']}")
            print(f"Compras: {c['compras']}")
            print(f"Total: {c['total']:.2f}")
            print(f"Desconto: {c['desconto']:.2f}")
            print(f"final: {c['final']:.2f}")
            print(f"Situação: {c['situacao']}")


        
