correo = input('Introduce un correo electrónico: ')

while '@' not in correo or '.' not in correo:
    print('Ingrese una dirección de correo válida')
    correo = input('Introduce un correo electrónico: ')

largo_del_correo = len(correo)
if '@' == correo[0] or '@' == correo[largo_del_correo - 1] or '.' == correo[0] or '@' == correo[largo_del_correo - 1]:
    print('Dirección de correo no válida')

else:
    print('Dirección de correo válida. Puede pasar.')