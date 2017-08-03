quantidade_cigarros = int(input("Quantidade de cigarros fumados por dia : "))
quantidade_anos = int(input("Quantidade de anos como fumante : "))

dias = quantidade_anos * 365
total_fumados = dias * quantidade_cigarros
total_dia = 24 * 6

total_dias_perdidos = total_fumados / total_dia

print("Total de dias perdidos : ", total_dias_perdidos)