# Programa jogo de adivinhacao
import random
num = int(input("Pense em um numero de 0 a 5: "))
computador = random.randint(0,5)
print("Voce escolheu o numero {}".format(num))
print("Saiu o numero {}".format(computador))
if num == computador:
    print("Parabens voce ganhou!")
else:
    print("Infelizmente vc perdeu! Tente mais uma vez...")
