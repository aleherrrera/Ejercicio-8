from Conjunto import Conjunto

def opcion0():
        print("Adiós")


def opcion1():
    Lista3 = Lista1 + Lista2
    Lista3.Mostrar()


def opcion2():
    Lista4 = Lista1 - Lista2
    Lista4.Mostrar()

def opcion3():
    Lista1 == Lista2

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':

    Lista1 = Conjunto()
    Lista2 = Conjunto()
    Lista3 = Conjunto()
    Lista4 = Conjunto()

    Lista1.Cargar()
    Lista2.Cargar()
    Lista1.Mostrar()
    Lista2.Mostrar()


    bandera = False  # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print("0 Salir")
        print("1. Union de los dos conjuntos")
        print("2. Diferencia de los dos conjuntos")
        print("3. Verificar si los conjuntos son iguales")
        opcion = int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion) == 0  # Si lee el 0 cambia la bandera a true y sale del menú
