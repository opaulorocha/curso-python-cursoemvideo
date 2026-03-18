maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f"Digite o {c}º peso (em kgs): "))

    if c == 1:  # primeira volta
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso eh {maior}")
print(f"O menor peso eh {menor}")
