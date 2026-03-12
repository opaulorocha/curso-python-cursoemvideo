# Programa para analisar se eh ou nao possivel formar um triangulo
ret1 = int(input("Digite o comprimento da reta 1: "))
ret2 = int(input("Digite o comprimento da reta 2: "))
ret3 = int(input("Digite o comprimento da reta 3: "))

if ret1 < ret2 + ret3 and ret2 < ret1 + ret3 and ret3 < ret1 + ret2:
    print("Com essas 3 retas eh possivel formar um triangulo!")
else:
    print("Com essas 3 retas nao eh possivel formar um triangulo!")


