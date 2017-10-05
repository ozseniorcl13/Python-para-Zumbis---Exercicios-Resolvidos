
preco = float(input('Preco : '))
desconto = float(input('Desconto : '))

preco *= 1 - desconto / 100

print('O novo preço é R$ {:.2f}'.format(preco))
