# Programa para calcular o custo de uma viagem
dist = float(input("Qual a distancia da viagem (Km)? "))

if dist >= 200:
    preco = dist * 0.45
else:
    preco = dist * 0.50
print("O valor da passagem a pagar sera de R${}".format(preco))
