# Programa ano bissexto
ano = int(input("Qual ano? "))
print(ano)
if ano % 4 == 0:
    print("O ano {} eh um ano bissexto!".format(ano))
else:
    print("O ano {} nao eh um ano bissexto!".format(ano))
