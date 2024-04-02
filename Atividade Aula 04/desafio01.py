valorCasa = float(input("Digite o valor do imovel: "))
salario = float(input("Digite seu salario: "))
anos = int(input("Digite o tempo em anos para pagamento do imovel: "))

percentualSalarial = salario * 0.3
meses = anos * 12
prestacaoMensal = valorCasa / meses

if prestacaoMensal > percentualSalarial:
    print(f"A prestação mensal foi de R${prestacaoMensal:.2f}, e 30% do seu salario é R${percentualSalarial:.2f}, portanto seu emprestimo foi negado")
else:
    print(f"Parabens, você teve o emprestimo aprovado")