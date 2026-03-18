# Programa para aprovar um emprestimo bancario para compra de uma casa
valor_casa = float(input("Qual eh o valor da casa? R$ "))
salario = float(input("Quanto eh o seu salario mensal? R$ "))
anos = int(input("Em quantos anos pretende pagar? "))
prest_mensal = (valor_casa/anos)/12
print("A sua prestacao mensal sera de R${:.2f}".format(prest_mensal))

if prest_mensal <= (salario*0.30):
    print("O seu emprestimo foi aprovado!")
else:
    print("O seu emprestimo nao foi aprovado!")
