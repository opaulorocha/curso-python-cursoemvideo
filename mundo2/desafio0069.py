import random
print("=-"*20)
print("Jogo Par ou Impar")
print("=-"*20)

total = par = impar = resultado = vitorias = 0
computador = 1

while True:
    n1 = int(input("Digite um valor: "))
    l = str(input("Par ou Impar? [P/I] ").upper())
    print("-" * 40)

    computador = random.randint(0,10)

    total = n1 + computador

    if total % 2 == 0:
        resultado = "Par"
        print(f"Voce jogou {n1} e o computador {computador}. Total de {n1 + computador}. Deu {resultado}.")
    else:
        resultado = "Impar"
        print(f"Voce jogou {n1} e o computador {computador}. Total de {n1 + computador}. Deu {resultado}.")

    print("-" * 40)

    if l == resultado.strip().upper()[0]:
        print("Voce venceu")
        print("Vamos jogar novamente...")
        print("=-" * 20)
        vitorias += 1
    else:
        print("Voce perdeu")
        break
print("=-"*20)
print(f"Game over, vc venceu {vitorias} vezes")












