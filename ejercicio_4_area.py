#Calcular el área de un polígono regular o de un círculo

import math

print('Este programa te permite obtener el área de cualquier figura geométrica (polígono regular).')
print('¿Cuántos lados tiene su figura?')
numero_de_lados = int(input('Círculo -> 0, Triángulo -> 3, Cuadrado -> 4, Pentágono -> 5 ... : '))

while numero_de_lados < 0 or numero_de_lados == 1 or numero_de_lados == 2:
    print('No existen figuras con ese número de lados.')
    print('Ingrese un número de lados correcto.')
    numero_de_lados = int(input())

if numero_de_lados == 0:
    print('Su figura es un círculo.')
    radio = float(input('Ingrese el radio de su círculo: '))
    while radio <= 0:
        print('Incorrecto. Ingrese un radio no negativo y diferente de 0.')
        radio = float(input())
    area = math.pi*(radio**2)
    print('El área de su cículo es: ' + str(area) + ' unidades cuadradas.')
elif numero_de_lados == 3:
    print('Su figura es un triángulo equilátero.')
    lado = float(input('Ingrese un lado de su triángulo: '))
    altura = float(input('Ingrese la altura de su triángulo: '))
    while lado <= 0 or altura <=0:
        print('Valores incorrectos.')
        lado = float(input('Ingrese un lado de su triángulo: '))
        altura = float(input('Ingrese la altura de su triángulo: '))
    area = (lado*altura)/2
    print('El área de su triángulo equilátero es de ' + str(area) + ' unidades cuadradas.')
elif numero_de_lados == 4:
    print('Su figura es un cuadrado.')
    lado = float(input('Ingrese un lado de su cuadrado: '))
    while lado <= 0:
        print('Los lados no pueden ser 0 o negativos.')
        lado = float(input('Ingrese un lado de su cuadrado: '))
    area = lado*lado
    print('El área de su cuadrado es de ' + str(area) + ' unidades cuadradas.')
else:
    print('Su figura es un polígono regular de ' + str(numero_de_lados) + ' lados.')
    lado = float(input('Ingrese un lado de su polígono regular'))
    while lado <= 0:
        print('Valor incorrecto.')
        lado = float(input('Ingrese un lado de su polígono regular'))
    perimetro = numero_de_lados*lado
    alfa = 360/numero_de_lados
    alfa_radianes = math.radians(alfa)
    apotema = (lado/2)/(math.tan(alfa_radianes/2))
    area = (perimetro*apotema)/2
    print('El área de su polígono regular de ' + str(numero_de_lados) + ' lados es de: ' + str(area) + ' unidades cuadradas.')