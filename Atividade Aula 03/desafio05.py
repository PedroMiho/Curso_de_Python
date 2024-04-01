retaA = int(input("Digite o tamanho da reta A: "))
retaB = int(input("Digite o tamanho da reta B: "))
retaC = int(input("Digite o tamanho da reta C: "))

somaAB = retaA + retaB
somaAC = retaA + retaC
somaBC = retaB + retaC

if somaAB > retaC and somaAC > retaB and somaBC > retaA: 
    print("Foi possivel formar o triangulo")
else:
    print("Não foi possivel formar o triangulo")