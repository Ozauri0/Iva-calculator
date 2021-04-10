################################################ Calcular iva ################################################################

primero = input ('Ingrese el valor ')

try:
   primero = int(primero)

except:
   primero = 'mucho texto'

if primero == 'mucho texto':
   print('Caracter incorrecto, ingresa un numero valido')
   
print(primero * 1.19)
