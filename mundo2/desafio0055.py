maior_idade = 0
menor_idade = 0
ano_atual = int(input("Digite o ano atual: "))
for c in range(1, 8):
    ano_nasc = int(input(f"Digite a sua data de nascimento (pessoa nº {c}): "))
    if ano_atual - ano_nasc >= 21:
       maior_idade += 1
    else:
        menor_idade += 1
print(f"{maior_idade} pessoas jah atingiram a maioridade. Enuanto {menor_idade} pessoas ainda sao menores de idade")

