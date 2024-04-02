n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 == n2:
    print("Não existe valor maior, pois ambos são iguais")

elif n1 > n2:
    print(f"O primeiro valor {n1} é o maior")

else:
    print(f"O segundo valor {n2} é o maior")