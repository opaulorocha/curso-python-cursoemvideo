n = contador = soma = 0
while True:
    n = int(input("Digite um numero [999 para parar]: "))
    if n == 999:
        break

    contador += 1
    soma += n
print(f"Foram digitados {contador} numeros. E a soma de todos eles eh {soma}")


