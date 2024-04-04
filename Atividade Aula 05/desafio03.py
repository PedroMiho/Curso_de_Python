soma = 0

for elemento in range (1, 501,1):
    multiplo3 = elemento % 3
    impar = elemento % 2
    
    if multiplo3 == 0 and impar == 1:
        print(f"O numero {elemento} é impar e multiplo de 3")
        soma = soma + elemento
else:
    print(f'A soma de todos os valores impares e multiplos  de 3 é igual a {soma}')