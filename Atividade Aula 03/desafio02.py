velocidade = int(input("Digite a velocidade do carro: "))
velocidadePermitida = 80
multaPorKm = 7

if velocidade > velocidadePermitida :
    velocidadeUltrapassada = velocidade - velocidadePermitida
    valorMulta = velocidadeUltrapassada * multaPorKm
    print(f"A sua velocidade foi de {velocidade} km/h, logo você foi multado em R${valorMulta},00")
else:
    print(f"A sua velocidade foi de {velocidade} km/h, então você não foi multado")
    