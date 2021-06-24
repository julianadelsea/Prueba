#4.leer un numero entero de dos digitos menor que 20 y determinar si es primo 
# print (f'Este programa sirva para determinar si un numero de dos digitos menor que 20 es primo')
# print(f'Ingrese el numero')
# numero = int (input())
# if numero < 0 : 
#   print (f'El numero es negativo y no sirve para este programa')
# digitosnumero = len (str(numero))
# if digitosnumero ==2 :
#   print (f'El numero que ingresó es apto')
# else: 
#   print (f'El numero que ingreso no es apto para este programa')


#6
# numero1 = input('Introduzca un numero: ')
# numero2 = input('introduzca otro numero: ')
# if len(str(numero1))== 2 and len(str(numero2))==2: 
#   print ('los numeros tienen dos digitos')
#   for numero in numero1,numero2: 
#     if numero == numero1 and numero ==numero2: 
#       print('los numeros son iguales')
#     else: 
#       print('Los numeros no son iguales')
# else: 
#   print ('No tienen dos digitos')

#7
# numero1 = input('Ingrese el primer numero: ')
# numero2 = input('Ingrese el segundo numero: ')
# if int(numero1) > int(numero2): 
#   print('El numero 1 es el mayor')
# else: 
#   print('El numero 2 es el mayor')

#8
# numero1 = input('Introduzca el primer numero: ')
# numero2 = input('Introuzca el segundo numero: ')
# if len(numero1) == 2 and len(numero2)==2:
#   print('los numeros tienen dos digitos')
#   resultado = 0 
#   for numero in numero1: 
#     resultado += int(numero) 
#   for numero in numero2: 
#     resultado += int(numero)
#     print(f"resultado es {resultado}")
# else: 
#   print('los numeros no tienen dos digitos')

#el siguiente es para hacer una suma completa, no de digito mas digito
# for numero in numero1, numero2: 
#   resultado += int(numero)
#   print(resultado)

#9
#leer un numero entero de tres digitos
#determinar en que posicion esta el mayor digito
# numero = input('introduzca un numero de tres digitos: ')
# if len(numero)==3: 
#   print('Tiene tres digitos')
#   digito1 = int(numero[0])
#   digito2 = int(numero[1])
#   digito3 = int(numero[2])
#   #primera solicion y mas facil que descubri muy tarde xd
#   maxi = max(digito1,digito2,digito3)
#   print(maxi)
  #segunda solucion
#   if digito1 > digito2 and digito1 > digito3:
#     print('El digito mayor es el 1')
#   elif digito2 > digito1 and digito2 > digito3:
#     print('El digito mayor es el 2')
#   else: 
#     print('El digito mayor es el 3')
# else: 
#   print('No tiene tres digitos')

#10

#11
numero1 = input('Introduzca el primer numero: ')
numero2 = input('Introduzca el segundo numero: ')
numero3 = input('Introduzca el tercer numero: ')
if len(numero1)==2 and len(numero2)==2  and len(numero3)==2: 
  print('Los numeros tienen dos digitos')
  digitos = {'digito1numero1' : int(numero1[0]) , 'digito2numero1' : int(numero1[1]) ,'digito1numero2' : int(numero2[0]) , 'digito2numero1 ': int(numero2[1]) ,'digito1numero3 ': int(numero3[0]) , 'digito2numero3' : int(numero3[1])}
  valores = digitos.values()
  
  print('El mayor digito entre los introducidos es: ' + str(max(valores)))
else: 
  print('Uno o mas de los numeros no tienen dos digitos')

#12




    





