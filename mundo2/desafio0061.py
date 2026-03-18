"""f = int(input("Digite um numero: "))
print(f"Voce pretende o fatorial de {f}! \nEntao...")
a = 1
c = 0
print(f"{f}! = ")
while f > 0:
    print(f"{c})
    a *= f
    f -= 1


print(f"o resultado final eh {a}")"""


f = int(input("Digite um numero: "))
print(f"Voce pretende o fatorial de {f}! \nEntao...")
c = f
a = 1
print(f"{f}! = ", end=" ")
while c > 0:
    print(f"{c}", end=" ")
    print(" x " if c > 1 else "=", end=" ")
    a *= c
    c -= 1
print(f"{a}")


