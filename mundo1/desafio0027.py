# Programa para verificar uma ocorrencia em uma string
frase = str(input("Digite uma frase: ").upper())
print("Aparecem na frase {} A's.".format(frase.count('A')))
print("O primeiro 'A' aparece na posicao {} e o ultimo 'A' aparece na posicao {}.".format(frase.find("A"), frase.rfind("A")))

