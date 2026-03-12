# Programa que calcula o preco final do aluguel de um carro
dias = int(input("Quantos dias voce alugou? "))
dist = int(input("Quantos km rodou? "))
total = (dias*60) + (dist*0.15)

print("O total a pagar eh de R${:.2f}".format(total))
