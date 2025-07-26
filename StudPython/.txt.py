# Guardando dados em arquivos .txt

# Etapa 1 Escrevendo um arquivo

# Abrir o arquivo no modo de escrita ('w' = write)
arquivo = open("Dados.txt", "w")

# Escreva no arquivo
arquivo.write("Olá, este é meu promeiro arquivo de texto.\n")
arquivo.write("Armazenando dados com Python é facil!\n")

# Fechar o arquivo para garantir que tudo foi salvo
arquivo.close()


# Etapa 2

# Ler de um arquivo

# Abririr o arquivo no modo de leitura ('r' = read)
arquivo = open("dados.txt", "r")

# Ler o conteuúdo
conteudo = arquivo.read()

# Mostrar no terminal
print(conteudo)

# Fechar o arquivo
arquivo.close()


# Etapa 3 Exemplos com cadastro de nomes

# Cadastro de nome idade

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))

# Salva o arquivo
with open("cadastro.txt", "a"):
    arquivo.write(f"{nome},{idade}\n")

# Ler o arquivo
print("Cadastro salvo com sucesso!")


