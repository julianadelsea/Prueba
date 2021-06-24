#CRUD 
base_datos =[]
def Crear_Usuario (nombre, cedula, edad): 
    nuevo_usuario = {
        'nombre': nombre,
        'cedula': cedula,
        'edad': edad
    }
    return nuevo_usuario

def Leer_Usuario (cedula,base_datos):
    resultado = {}
    for usuario in base_datos:
        if usuario ['cedula']== cedula :
            resultado = usuario
    print(resultado)

print('-------------------------')
print ('APLICACION CRUD')
print ('1. Crear usuario')
print ('2. Buscar Usuario')
print('-------------------------')
print('                 ')
opcion = 0
while opcion != 9: 
    opcion = int(input('ingrese la opcion: '))
    if opcion ==1: 
        nombre = input('Ingrese el nombre: ')
        cedula = int(input('Ingrese la cedula: '))
        edad = int(input('Ingrese la edad: '))
        base_datos.append(Crear_Usuario(nombre,cedula,edad))
    elif opcion ==2:
        cedula = int(input('Ingrese la cedula: '))
        Leer_Usuario(cedula,base_datos)


