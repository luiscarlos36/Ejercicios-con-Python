import math

def calcula_raiz(num):
    if num < 0:
        raise ValueError ('El número no puede ser negativo')

    else:
        return math.sqrt(num)

op = int(input('Introduce un número: '))

try:
    print(calcula_raiz(op))

except ValueError as ErrorDeNumeroNegativo:
    print('Error de número negativo.')

print('Programa terminado.')