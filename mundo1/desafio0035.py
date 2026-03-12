# Programa aumentos multiplos
salario = float(input("Qual o salario do funcionario? R$"))
aumento1 = salario + salario * 0.10
aumento2 = salario + salario * 0.15

if salario >= 1250:
    print("O seu novo salario sera de R${}".format(aumento1))
else:
    print("O seu novo salario sera de R${}".format(aumento2))
