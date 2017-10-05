salario = float(input('Salario : '))
p_aumento = float(input('Porcentagem do aumento : '))/100

salario *= 1 + p_aumento

print('O novo salário com {:.2f}% de aumento é R${:.2f}'.format(p_aumento * 100, salario))
