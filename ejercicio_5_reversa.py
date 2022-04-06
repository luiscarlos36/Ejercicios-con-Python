#Hacer una cadena o una lista en reversa.

cadena = input('Ingrese una cadena de caracteres: ')

for i in range(len(cadena) -1, -1, -1):
    print(cadena[i], end='')

print()
print(cadena)
print(cadena[:])
print()
print(cadena[::-1]) # [0:10] desde 0 hasta 10, por defecto incrementa de 1 en 1, pero [0:10:-1] hace que decremente.