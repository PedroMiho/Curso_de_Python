primeiroTermo = int(input("Digite um termo: "))
razao = int(input("Digite a razao: "))

ultimoTermo = (primeiroTermo + (10 - 1) * razao) + razao

for elemento in range (primeiroTermo, ultimoTermo, razao) :
    print(elemento, end=' -> ')
else:
    print("FIM")