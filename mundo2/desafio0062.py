primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))

c = 1
termo = primeiro_termo

while c <= 10:
     print(termo, end=" ")
     termo += razao
     c += 1
