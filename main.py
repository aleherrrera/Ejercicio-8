from ColeccionEmpleados import ArregloEmpleados
from Interfaces import ITesorero
from Interfaces import IGerente

def Gerente(manejadorGerente):
    def opcion0():
        print('Saliendo')
    def opcion1():
        try:
            dni = int(input('Ingresar DNI del empleado: '))
            nuevo=float(input('Ingresar el nuevo basico: $'))
            manejadorGerente.modificarBasicoEPlanta(dni,nuevo)
        except IndexError:
            print('DNI incorrecto')

    def opcion2():
        try:
            dni = int(input('Ingresar DNI del empleado: '))
            nuevo=float(input('Ingresar el nuevo viatico: $'))
            manejadorGerente.modificarViaticoEExterno(dni,nuevo)
        except IndexError:
            print('DNI incorrecto')

    def opcion3():
        try:
            dni = int(input('Ingresar DNI del empleado: '))
            nuevo=float(input('Ingresar el nuevo valor por hora: $'))
            manejadorGerente.modificarValorEPorHora(dni,nuevo)
        except IndexError:
            print('DNI incorrecto')

    switcher = {
        0: opcion0,
        1: opcion1,
        2: opcion2,
        3: opcion3
    }
    def switch(argument):
        func = switcher.get(argument, lambda: print("Opción incorrecta"))
        func()

    bandera = False  # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("\nMENU GERENTE")
        print("0. Salir")
        print("1. Modificar basico de planta")
        print("2. Modificar viatico de externo")
        print("3. Modificar valor por hora")
        opcion = int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion) == 0  # Si lee el 0 cambia la bandera a true y sale del menú

def Tesorero(manejadorTesorero):
    try:
        dni = int(input('Ingresar DNI del empleado: '))
        manejadorTesorero.gastosSueldoPorEmpleado(dni)
    except IndexError:
        print('DNI incorrecto')

def opcion0():
    print("Adiós")

def opcion1():
    try:
        Empleados.RegistrarHoras()
    except IndexError:
        print('DNI incorrecto')
def opcion2():
    try:
        Empleados.Tarea()
    except AttributeError:
        print('Tarea incorrecta')

def opcion3():
    Empleados.Ayuda()

def opcion4():
    Empleados.MostrarSueldos()

def opcion5():
    usuario = input('Usuario: ')
    clave = input('Clave: ')
    if usuario == 'uTesoreso' and clave == 'ag@74ck':
        Tesorero(ITesorero(Empleados))
    else:
        print('Usuario o clave incorrecto')

def opcion6():
    usuario = input('Usuario: ')
    clave = input('Clave: ')
    if usuario == 'uGerente' and clave == 'ufC77#!1':
        Gerente(IGerente(Empleados))
    else:
        print('Usuario o clave incorrecto')

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
    5: opcion5,
    6: opcion6
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':

    Empleados = ArregloEmpleados(6)

    Empleados.cargaExterno()
    Empleados.cargaPlanta()
    Empleados.cargarContratado()

    bandera = False # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print("0. Salir")
        print("1. Registrar horas")
        print("2. Total de tarea")
        print("3. Ayuda")
        print('4. Mostrar sueldo')
        print('5. Funciones Tesorero')
        print('6. Funciones Gerente')
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú