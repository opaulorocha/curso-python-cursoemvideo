# Programa radar eletronico
velocidade = float(input("Qual a velocidade do carro? "))
#multa = (velocidade - 80) * 7
print("Voce esta a {} Km/h!".format(velocidade))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Voce ultrapassou o limite de velocidade de 80 Km/h. Entao sera multado em {} reais". format(multa))

