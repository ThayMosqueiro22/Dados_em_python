#Criando um arquivo para teste

with open (".txt", "w") as arquivo:
    arquivo.write("Python é uma linguagem poderosa.\n")
    arquivo.write("Estamos aprendendo arquivos.")

with open (".txt","r") as arquivo:
    conteudo = arquivo.read()

    print(conteudo)


#Lendo linha por linha 

with open (".txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())


