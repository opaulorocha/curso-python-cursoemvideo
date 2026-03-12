# Programa para verificar o primeiro e ultimo nome de uma pessoa
nome = str(input("Digite o seu nome completo: "))
print(nome)
print(nome.split())
print("Primeiro = {}".format(nome.split()[0]))
print("Ultimo = {}".format(nome.split()[-1]))