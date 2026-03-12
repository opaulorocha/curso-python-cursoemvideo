# Programa para o cosseno, seno e tangente de um angulo
import math
angulo = float(input("Digite o valor do angulo: "))
numcos = math.cos(math.radians(angulo))
numsen = math.sin(math.radians(angulo))
numtan = math.tan(math.radians(angulo))
print("O cosseno, seno e tangente do angulo {}, sao respectivamente {:.2f}, {:.2f} e {:.2f}.".format(angulo, numcos, numsen, numtan))

