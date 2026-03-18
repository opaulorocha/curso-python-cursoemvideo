prec = float(input("Preco total das compras: R$"))
pag = int(input("Qual a condicao de pagamento? Digite...\n 1- Ah vista em dinheiro/cheque\n 2- Ah vista no cartao\n 3- 2x no cartao \n 4- 3x ou mais no cartao \n Qual a opcao? "))
prec_final = 0
if pag == 1:
    prec_final = prec - prec * 0.10
elif pag == 2:
    prec_final = prec - prec * 0.05
elif pag == 3:
    prec_final = prec/2
    print(f"Sua compra sera parcelada em 2x de R${prec_final:.2f}.")
elif pag == 4:
    parcelas = int(input("Quantas parcelas? "))
    prec_final = prec + prec * 0.2
    print(f"Sua compra sera parcelada em {parcelas}x de {prec_final/parcelas:.2f} com juros.")
else:
    prec_final = prec
    print("Opcao invalida, tente novamente.")
print(f"Sua compra de R${prec} vai custar R${prec_final:.2f} reais no final.")

