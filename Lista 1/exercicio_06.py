distancia = float(input('Distancia em metros : '))
vm = float(input("Velocidade media em km/h : "))

vm /= 3.6 
tempo = distancia/vm

print("Tempo : ", tempo)