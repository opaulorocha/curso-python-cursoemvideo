# Programa para sortear uma item na lista
import random
nome1 = str(input("Digite o nome do aluno 1: "))
nome2 = str(input("Digite o nome do aluno 2: "))
nome3 = str(input("Digite o nome do aluno 3: "))
nome4 = str(input("Digite o nome do aluno 4: "))

nomes = [nome1, nome2, nome3, nome4]
sorteio = random.choice(nomes)
print("O aluno sorteado para ir apagar o quadro eh o/a {}.".format(sorteio))

