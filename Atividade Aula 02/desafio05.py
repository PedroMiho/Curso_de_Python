nomeCompleto = "Ana Clara dos santos"

divideNome = nomeCompleto.split()
primeroNome = divideNome[0]
ultimoNome = divideNome[-1]
totalItem = len(divideNome)

print(f"O primeiro nome é {primeroNome}")
print(f"O ultimo nome é {divideNome[totalItem-1]}")
