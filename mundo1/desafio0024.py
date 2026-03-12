# Programa para separar digitos de um numero
num = int(input("Digite um numero de 0 a 9999: "))
print(f"analisando o numero {num}...")
print(f"Milhar: {num//1000}")
print(f"Centena: {(num%1000)//100}")
print(f"Dezena: {(num%100)//10}")
print(f"Unidade: {num%10}")


