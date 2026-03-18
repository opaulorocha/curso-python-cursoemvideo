# Programa que converte um numero inteiro para binario, octal ou hexadecimal
num = int(input("Digite um numero: "))
base = int(input("Qual base de convesao vc pretende converter o numero {}? \nAperte... \n1- Binario\n2- Octal\n3- Hexadecimal\n".format(num)))

if base == 1:
    print(f"O numero {num} convertido para binario eh {bin(num)[2:]}")

elif base == 2:
    print(f"O numero {num} convertido para octal eh {oct(num)[2:]}")

elif base == 3:
    print(f"O numero {num} convertido para hexadecimal eh {hex(num).upper()[2:]}")
else:
    print("Opcao errada, tente novamente")

