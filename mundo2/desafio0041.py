n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
media = (n1+n2)/2
print(f"A sua media foi de {media:.2f}")
if media < 5:
    print("Reprovado!")
elif 5 <= media <= 6.9:
    print("Recuperacao!")
else:
    print("Aprovado!")
