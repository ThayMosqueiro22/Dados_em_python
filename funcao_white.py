with open ("Escala de Pontuação (1 a 5).txy", "w") as arquivo:
    arquivo.write("Relatório de vendas\n")
    arquivo.write("Total: 1500")

with open("Escala de Pontuação (1 a 5).txy", "a") as arquivo:
    arquivo.write("\nNovo registro adicionado.")

with open ("Escala de Pontuação (1 a 5).txy", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())