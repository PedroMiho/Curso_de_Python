distanciaUsuario = float(input("Digite a distancia a ser percorrida: "))
distanciaMaxima = 200
acima200 = 0.45
abaixo200 = 0.50

if distanciaUsuario > distanciaMaxima:
    valor = distanciaUsuario * acima200
    print(f"O valor vai ser de R${valor}")
else: 
    valor = distanciaUsuario * abaixo200
    print(f"O valor vai ser de R${valor}")