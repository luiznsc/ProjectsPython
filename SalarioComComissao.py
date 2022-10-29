#Uma organização oferece um salário fixo e uma
#comissão que varia em função das vendas. Se o
#funcionário exceder R$ 5000,00 a comissão é de 12% do
#excedente, caso contrário ele não recebe nada. Crie um
#programa que cálculo a comissão do vendedor em função
#das suas vendas. 


vendas = int(input("Digite o valor de vendas do funcionario:"))
fixo = 2000
comissao = 0.12

if vendas > 5000:
        print("Para este valor de vendas a comissão é de 12%.")
        salario = fixo + (vendas * comissao)
        print(f"\nAssim, o valor total do salário será: R${salario}")
else:
    print(f"Para este valor de vendas não há comissão.")