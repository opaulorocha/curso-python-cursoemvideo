from datetime import date
data_nascimento = int(input("Digite o ano do seu nascimento: "))

data_atual = date.today().year
idade = data_atual - data_nascimento

print(f"atualmente vc tem {idade} anos em {data_atual}")
if idade < 18:
    print(f"ainda nao vai se alistar. Faltam {18-idade} anos")
elif idade == 18:
    print("Esta na hora de se alistar")
else:
    print(f"Ja passou a hora de se alistar. Ja se passaram {idade-18} anos")


