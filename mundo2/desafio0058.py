
sex = 0

while not (sex == "M" or sex == "F"):
    sex = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
    #print(sex)

    if sex != "M" and sex != "F":
        print("Errou, digite novamente.")
    else:
        print(f"Sexo {sex} registrado com sucesso.")


"""sex = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
#ou
while sex not in "mMfF":
    sex = str(input("Errou, digite novamente: ")).strip().upper()
print(f"Sexo {sex} regitrado com sucesso.")"""
