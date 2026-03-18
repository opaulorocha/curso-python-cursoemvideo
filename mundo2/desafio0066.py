n = contador = media = soma = mais = maior = menor = 0
while not mais == "N":
    n = int(input("Digite um numero: "))
    contador += 1
    soma += n
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        else:
            menor = n
    mais = str(input("Pretende continuar? [S/N] ")).strip().upper()[0]
media = soma/contador
print(f"Voce digitou {contador} e a media deles eh {media}")
print(f"O maior numero de todos eh o {maior} e o menor eh {menor}")



