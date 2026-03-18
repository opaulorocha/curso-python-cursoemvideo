media_idade = 0
menoridade_mulher = 0
maior_idade = 0
nome_homem_mais_velho = 0

for c in range(1, 5):
    nome = str(input(f"Digite o {c}º nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o seu sexo: "))

    media_idade += idade / 4
    if sexo == "M" or sexo == "m" or sexo == "Masculino" or sexo == "masculino":
        if c == 1:
            maior_idade = idade
            nome_homem_mais_velho = nome
        else:
            if idade > maior_idade:
                maior_idade = idade
                nome_homem_mais_velho = nome

    if (sexo == "F" or sexo == "Feminino" or sexo == "feminino" or  sexo == "f") and (idade < 20):
        menoridade_mulher += 1
print(f"a media das idades das 4 pessoas eh de {media_idade:.2f} anos.")
print(f"Temos {menoridade_mulher} mulheres com menos de 20 anos")
print(f"O homem mais velho eh o {nome_homem_mais_velho} com {maior_idade} anos.")
