nota1 = float(input("Digite a primeira nota entre 0 a 10: "))
nota2 = float(input("Digite a segunda nota entre 0 a 10: "))

if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
    print("Foi")

    media = (nota1 + nota2) / 2

    if media >= 7 :
        print(f"A sua média foi de {media}, logo você foi aprovado")

    elif media >= 5 :
        print(f"A sua média foi de {media}, logo você foi para recuperação")

    else :
        print(f"A sua média foi de {media}, logo você foi reprovado")

else :
    print("Digite uma nota valida")

