from datetime import *

dataAtual = date.today()
anoAtual = dataAtual.year
mesAtual = dataAtual.month
diaAtual = dataAtual.day

print(dataAtual)
print(anoAtual)
print(mesAtual)
print(diaAtual)

anoNascimento = int(input("Digite o seu ano de nascimento: "))

idade = anoAtual - anoNascimento

if idade <= 9:
    print("CATEGORIA MIRIM")
elif idade <= 14:
    print("CATEGORIA INFANTIL")
elif idade <= 19 :
     print("CATEGORIA JUNIOR")
elif idade <= 24:
    print("CATEGORIA SÊNIOR")
else:
    print("CATEGORIA MASTER")
    