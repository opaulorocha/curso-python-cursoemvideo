ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"Voce tem {idade} anos!")

if idade <= 9:
    print("Voce esta na categoria mirim!")
elif idade <= 14:
    print("Vc esta na categoria infantil!")
elif idade <= 19:
    print("Voce esta na categoria junior!")
elif idade <= 25:
    print("Voce esta na categoria senior!")
else:
    print("Voce esta na categoria master!")
