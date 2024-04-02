from random import choice

opcoes = ["PEDRA", "PAPEL", "TESOURA"]
escolhaMaquina = choice(opcoes)
print(escolhaMaquina)

escolhaUsuario = input("Informe a sua escolha: ").upper()

if escolhaMaquina == escolhaUsuario:
    print(f"AMBOS ESCOLHERAM {escolhaMaquina}, PORTANTO DEU EMPATE")

elif escolhaMaquina == "PEDRA" and escolhaUsuario == "TESOURA":
    print(f"A MAQUINA ESCOLHEU {escolhaMaquina}, PORTANTO ELA VENCEU")

elif escolhaMaquina == "PAPEL" and escolhaUsuario == "PEDRA":
    print(f"A MAQUINA ESCOLHEU {escolhaMaquina}, PORTANTO ELA VENCEU")
    
elif escolhaMaquina == "TESOURA" and escolhaUsuario == "PAPEL":
    print(f"A MAQUINA ESCOLHEU {escolhaMaquina}, PORTANTO ELA VENCEU")

elif escolhaMaquina == "PEDRA" and escolhaUsuario == "PAPEL":
    print(f"VOCÊ ESCOLHEU {escolhaUsuario}, PORTANTO VOCÊ VENCEU")

elif escolhaMaquina == "PAPEL" and escolhaUsuario == "TESOURA":
    print(f"VOCÊ ESCOLHEU {escolhaUsuario}, PORTANTO VOCÊ VENCEU")
    
elif escolhaMaquina == "TESOURA" and escolhaUsuario == "PEDRA":
    print(f"VOCÊ ESCOLHEU {escolhaUsuario}, PORTANTO VOCÊ VENCEU")
    
else:
    print(f"A OPÇÃO ESTA INCORRETA")