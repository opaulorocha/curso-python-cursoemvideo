# revisar
num = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezasseis", "dezessete", "dezoito", "dezenove", "vinte")

for c in range(0, len(num)):
    c = int(input("Digite um numero: "))

    while c > 20 or c < 0:
        print("Tente novamente.")
        c = int(input("Digite um numero: "))

    print(f"Voce digitou o numero {num[c]}")
    break
print("Fim")

