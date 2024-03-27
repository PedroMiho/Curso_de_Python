# DESAFIO 01
# Crie um programa que leia o nome completo de uma pessoas e mostre:

# O nome com todas as letras maiúsculas

# O nome com todas as letras minúsculas

# Quantas letras ao todo (sem considerar espaços)

# Quantas letras tem o primeiro nome

nomeCompleto = input("Digite seu nome completo: ")

nomeMaiusculo = nomeCompleto.upper()
nomeMinusculo = nomeCompleto.lower()
nomeSemEspaco = nomeCompleto.replace(" ", "")
divideNome = nomeCompleto.split()

print(nomeMaiusculo)
print(nomeMinusculo)
print(len(nomeSemEspaco))
print(len(divideNome[0]))