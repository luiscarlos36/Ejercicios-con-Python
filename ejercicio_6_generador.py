'''
def genera_pares(limite):
    num = 1
    mi_lista = []

    while num < limite:
        mi_lista.append(num * 2)
        num += 1

    return mi_lista

print(genera_pares(10))
'''

'''
def genera_pares(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1

devuelve_pares = genera_pares(10)

print(next(devuelve_pares))
print('Aquí podría ir más código... ')
print(next(devuelve_pares))
print('Aquí podría ir más código... ')
print(next(devuelve_pares))
print('Aquí podría ir más código... ')
print(next(devuelve_pares))
'''

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas = devuelve_ciudades('Madrid', 'Barcelona', 'Bilbao', 'Valencia')
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))