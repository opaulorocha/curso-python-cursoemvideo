# Programa jogo de adivinhacao
import random
cont_palpites = 0
num = 0
computador = 1
#acertou = False
while num != computador:
#while not acertou:
    num = int(input("Pense em um numero de 0 a 10: "))

    computador = random.randint(0,10)
    print("Voce escolheu o numero {}".format(num))
    print("Saiu o numero {}".format(computador))

    cont_palpites += 1

    if num == computador:
        print("Parabens voce ganhou!")
    else:
        print("Infelizmente vc perdeu! Tente mais uma vez...")
print(f"Para acertar voce tentou {cont_palpites} vezes")