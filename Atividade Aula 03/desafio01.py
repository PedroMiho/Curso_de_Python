from random import *

numeroMaquina = randint(0, 5)
print(numeroMaquina)
numeroUsuario = int(input("Digite um numero de 0 a 5:") )

if numeroMaquina == numeroUsuario:
    print(f"O numero sorteado foi {numeroMaquina}, parabens você ganhou")
else:
    print(f"O numero sorteado foi {numeroMaquina}, você errou, tente novamente")