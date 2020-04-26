from typing import List, Any


class Conjunto:

    __numeros = []
    __cantidad = 0

    def __init__(self,cantidad=0):
        self.__numeros = []

    def Agregar(self,numero):
        return self.__numeros.append(numero)

    def Cargar(self):
        print('Ingresar cantidad de numeros para el conjunto')
        cant = int(input())
        print('Ingrese {} numeros enteros'.format(cant))
        for i in range(cant):
            numero = int(input())
            self.__numeros.append(numero)

    def getCant(self):
        return len(self.__numeros)

    def getNum(self,indice):
        return self.__numeros[indice]

    def Mostrar(self):
            print(self.__numeros)

    def __add__(self, otra):
        lista = Conjunto()
        for i in range(self.getCant()):
            lista.Agregar(self.getNum(i))
        for i in range(otra.getCant()):
            a=0
            for j in range(lista.getCant()):
                if otra.getNum(i)==lista.getNum(j):
                    a=1
            if a == 0:
                lista.Agregar(otra.getNum(i))
        return lista

    def __sub__(self, otra):
        lista = Conjunto()
        for i in range(self.getCant()):
            a=0
            for j in range(otra.getCant()):
                if self.getNum(i)==otra.getNum(j):
                    a=1
            if a == 0:
                lista.Agregar(self.getNum(i))
        return lista

    def __eq__(self, otro):
        if self.getCant() == otro.getCant():
            a=0
            for i in range(self.getCant()):
                for j in range(otro.getCant()):
                    if self.getNum(i) == otro.getNum(j):
                        a+=1
            if a == self.getCant():
                print('Los conjuntos son iguales')
            else:
                print('Los conjuntos no son iguales')

        else:
            print('Los conjuntos no tienen la misma cantidad de elemnentos')

