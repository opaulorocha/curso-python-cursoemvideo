# Programa para calcular a quantidade de tinta para pintura
alt = float(input("Qual a altura? (em metros): "))
lar = float(input("Qual a largura? (em metros): "))

area = alt*lar
tinta = area/2

print("Temos {} m2 de area. Entao precisamos de {} litros de tinta para pintar.".format(area, tinta))
