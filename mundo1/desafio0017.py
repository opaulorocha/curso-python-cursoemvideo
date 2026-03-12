# Programa para demonstrar a parte inteira de um numero
import math
num = float(input("Digite um numero real: "))
numint = math.trunc(num)
print("O numero {} tem a parte inteira {}.".format(num, numint))
