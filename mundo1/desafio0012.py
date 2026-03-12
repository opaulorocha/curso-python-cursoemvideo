# Calculo de desconto do preco de um produto
prod = float(input("Qual o preco do produto? "))
desc = prod - (prod*0.05)

print("O novo preco com desconto de 5% sera {:.2f} reais.".format(desc))
