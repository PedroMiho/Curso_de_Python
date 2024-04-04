soma = 0

for elemento in range (1, 7):
    numero = int(input(f"Digite o {elemento}° valor: "))
    
    resto = numero % 2
    
    if resto == 0:
        soma = soma +  numero
else:
    print(f"A soma dos valores pares digitados foi igual a {soma}")