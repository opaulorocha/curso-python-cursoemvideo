# Programa para calcular a hipotenusa
import math
cop = float(input("Digite o valor do cateto oposto (cm): "))
cadj = float(input("Digite o valor do cateto adjacente (cm): "))
hip = math.hypot(cop, cadj)
print("O valor da hipotenusa eh de {:.2f}".format(hip))

