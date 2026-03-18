primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
decimo_termo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo_termo + razao, razao):
    print(c)
print("fim")


