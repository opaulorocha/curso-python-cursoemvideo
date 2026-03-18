
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

num = 0
#num = int(input("O que vc quer fazer com ele? \n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos numeros \n [5] Sair do programa \n "))

while num != 5:
    num = int(input("O que vc quer fazer com ele? \n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos numeros \n [5] Sair do programa \n "))

    if num == 1:
        print(f"a soma entre {n1} e {n2} eh {n1 + n2}")
    elif num == 2:
        print(f"a multiplicacao entre {n1} e {n2} eh {n1 * n2}")
    elif num == 3:
        if n1 > n2:
            print(f"O maior numero eh {n1}")
        elif n2 > n1:
            print(f"O maior numero eh o {n2}")
        else:
            print("Os numeros sao iguais")
    elif num == 4:
        print("Digite novos numeros")
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o primeiro numero: "))
    elif num == 5:
        print("Voce saira do programa...")
    else:
        print("Opcao invalida. Tente novamente.")

    print("="*35)
print("Saiu...")



