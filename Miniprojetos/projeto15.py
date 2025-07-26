# Mini projeto

# Cadastro e logi

# Cadastro de usuario
usuarios = []

def cadastro_usuario():
    nome = input("Digite o nome de usuario:")
    senha = input("Digite a senha:")
    usuario = {"nome":nome,"senha":senha }
    usuarios.append(usuario)
    print("Usuario cadastrado com sucesso.")
# Login de Usuario

def login_usuario():
    print("=== Sistema de Login ===")

    for usuario in usuarios:

     tentativas = 3

    while tentativas > 0:
     nome = input("Nome de usuario:")
     senha = input("Sua senha:")

    if nome in usuarios and usuarios[nome] == senha:
     print("Login realizado com sucesso.")
     
    else: 
       tentativas -= 1
       print(f"Dados incorretos. Tentativas {tentativas}")
   
    print("Numero de tentativas excedido. acesso bloqueado")
    return
# Menu 

while True:
   print("\n=== Menu ===")
   print("1- Cadastra-se")
   print("2- login")
   print("3- Sair")

   opcao = input("Escolha uma opção:")

   if opcao == '1':
      cadastro_usuario()
   elif opcao == '2':
      login_usuario()
   elif opcao == '3':
      ("Fim do programa. tchau")
      break
   else:
      print("Opção invalida. tente novamente.")