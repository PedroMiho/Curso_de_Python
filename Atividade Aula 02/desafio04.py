frase = input("Digite uma frase: ").upper()

contaCaracter = frase.count("A")
inicioCaracter = frase.find("A")
ultimoCaracter = frase.rfind("A")

print(f"A letra A apareceu {contaCaracter} vezes")
print(f"A letra A apareceu na {inicioCaracter + 1} posição")
print(f"A letra A apareceu pela ultima vez na {ultimoCaracter + 1} posição")