s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 2 == 1 and c % 3 == 0:
        s += c
        cont += 1
print("Fim da contagem")
print(f"a soma total de {cont} numeros, sera de {s}")
