primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
#uant_termos = int(input("uantos termos vc pretende: "))
c = 1
termo = primeiro_termo
mais = 10
total = 0
while mais != 0:
     total += mais
     while c <= total:
          print(termo, end=" ")
          termo += razao
          c += 1
     print("Pausa")
     mais = int(input("uantos termos vc uer contar mais? "))
print("Fim")
print(f"Foram pedidos {total} termos.")