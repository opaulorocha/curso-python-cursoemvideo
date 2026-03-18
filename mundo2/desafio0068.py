# Tabuada
"""n = int(input("Quer ver a tabuada de qual valor: "))
print("="*25)
c = 0
while c < 10:
    c += 1
    print(f"{n} x {c} = {n * c}")

    #n = int(input("Quer ver a tabuada de qual valor: "))
    #print("=" * 25)
print("="*25)"""

n = c = 0

while True:
    print("=" * 25)
    n = int(input("Quer ver a tabuada de qual valor: "))
    print("=" * 25)

    if n <= 0:
        break
    c = 1
    while c <= 10:
        print(f"{n} x {c} = {n * c}")
        c += 1
print("Programa tabuada encerrado. Volte sempre")



