# comparacao de numeros
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
maior = 0
menor = 0

if num1 > num2:
    maior = num1
    menor = num2
    print(f"{num1} e {num2}, o {num1} eh o primeiro valor. {maior} eh maior")
elif num1 < num2:
    maior = num2
    menor = num1
    print(f"{num1} e {num2}, o {num2} eh o segundo valor. {maior} eh maior")
else:
    print("Nao existe nem maior e nem menor, os numeros sao iguais")




