qnt_homens = qnt_mulheres = maior = idade = sexo = continuar = 0

while True:
    print("=-" * 20)
    print("        CADASTRE UMA PESSOA     ")
    print("=-" * 20)

    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F] ").strip().upper()[0])
    while sexo not in ("F", "M"):
        sexo = str(input("Sexo: [M/F] "))
    print("-" * 20)

    continuar = str(input("Quer continuar? [S/N] ").strip().upper()[0])
    while continuar not in ("S", "N"):
        continuar = str(input("Quer continuar? [S/N] ").strip().upper()[0])

    if continuar == "N":
        break

    if idade >= 18:
        maior += 1
    if sexo == "M":
        qnt_homens += 1
    if sexo == "F" and idade <= 20:
        qnt_mulheres += 1

print(f"Total de pessoas com mais de 18 anos: {maior}")
print(f"Ao todo temos {qnt_homens} homens cadastrados")
print(f"E temos {qnt_mulheres} mulheres com menos de 20 anos")



