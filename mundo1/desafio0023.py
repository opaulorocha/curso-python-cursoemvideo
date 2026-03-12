# Programa analisador de textos
nome = str(input("Digite um nome: ")).strip()
print("Analisando seu nome...")
print("O seu nome em maisculo: {}".format(nome.upper()))
print("O seu nome em minusculo: {}".format(nome.lower()))
print("O seu nome tem ao todo {} letras.".format(len(nome) - nome.count(" ")))
print("O seu primeiro nome tem {} letras.".format(nome.find(" ")))













