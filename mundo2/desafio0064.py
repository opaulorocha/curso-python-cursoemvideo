# serie fibonacci

anterior = contador = proximo = 0
atual = 1

n = int(input("Digite quantos termos deseja mostrar: "))
while contador < n:
    print(anterior, end=" ")
    proximo = anterior + atual
    #print(proximo, end=" ")
    anterior = atual
    atual = proximo
    contador += 1
