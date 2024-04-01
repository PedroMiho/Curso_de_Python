n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

if n1 > n2 and n1 > n3:
    print(f"O maior valor foi: {n1}")
elif n2 > n3:
    print(f"O maior valor foi: {n2}")
else :
    print(f"O maior valor foi: {n3}")

if n1 < n2 and n1 < n3:
    print(f"O menor valor foi: {n1}")
if n2 < n1 and n2 < n3:
    print(f"O menor valor foi: {n2}")
if n3 < n1 and n3 < n2:
    print(f"O menor valor foi: {n3}")