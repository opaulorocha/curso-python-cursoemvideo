print("=-" * 20)
print("        LOJA SUPER BARATAO     ")
print("=-" * 20)

total = preco = mais_mil_reais = menor_preco = nome_mais_barato = 0
primeiro = True
while True:
    nome_produto = str(input("Nome do produto: "))
    preco = float(input("Preco: R$"))
    total += preco

    continuar = str(input("Quer continuar? [S/N] ").strip().upper()[0])

    while continuar not in ("S", "N"):
        continuar = str(input("Quer continuar? [S/N] ").strip().upper()[0])

    if preco >= 1000:
        mais_mil_reais += 1

    if primeiro:
        menor_preco = preco
        nome_mais_barato = nome_produto
        primeiro = False
    else:
        if preco < menor_preco:
            menor_preco  = preco
            nome_mais_barato = nome

    if continuar == "N":
        break

print("="*20, "FIM DO PROGRAMA", "="*20)
print(f"O total da compra foi de {total:.2f}")
print(f"Temos {mais_mil_reais} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {menor_preco} ue custa R${nome_mais_barato}")