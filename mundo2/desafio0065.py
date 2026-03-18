n = int(input("Digite um numero [999 para parar]: "))
contador = soma = 0

while n != 999:
    contador = contador + 1
    soma = soma + n
    n = int(input("Digite um numero [999 para parar]: "))
print(f"Voce digitou {contador} e a soma de todos eles eh {soma}")