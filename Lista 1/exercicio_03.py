dias = int(input("Quantidade de dias : "))
horas = int(input("Quantidade de horas : "))
minutos = int(input("Quantidade de minutos : "))
segundos = int(input("Quantidade de segunds : "))

dias *= 24 * 3600
horas *= 3600
minutos *= 60

total_segundos = dias + horas + minutos
print("Total em segundos : % 's", total_segundos)