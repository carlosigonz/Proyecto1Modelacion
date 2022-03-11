import csv

from sympy import false

grafo = []
ciudades = {}
indice_ciudad = {}
lista_ciudad = []


class Ciudad:
    def __init__(self, nombre, codigo, visa):
        self.nombre = nombre
        self.codigo = codigo
        self.visa = visa


def menu():
    leer_ciudades("Datos Ciudades.csv")
    leer_rutas("Datos Rutas.csv")
    print_grafo(grafo)
    print("Bienvenido a Metro Travel.")
    ciudad_origen = input("Escriba el nombre de la ciudad origen\n")
    seguir = False
    while seguir == False:
        for i in lista_ciudad:
            if ciudad_origen.lower() == i.lower():
                seguir = True
                break
        if seguir == False:
            ciudad_origen = input(
                "El nombre de la ciudad no es correcto, por favor escriba el nombre de la ciudad origen\n")

    ciudad_destino = input("Escriba el nombre de la ciudad destino\n")
    seguir = False
    while seguir == False:
        for i in lista_ciudad:
            if ciudad_destino.lower() == i.lower():
                seguir = True
                break
        if seguir == False:
            ciudad_destino = input(
                "El nombre de la ciudad no es correcto, por favor escriba el nombre de la ciudad destino\n")

    tiene_visa
    num = input(
        "Escriba el número según corresponda\n1.Tiene Visa\n2.No tiene Visa")
    while num < 1 | num > 2:
        num = input(
            "El número que ha ingresado no es correcto. Por favor escriba el número según corresponda\n1.Tiene Visa\n2.No tiene Visa")
    if num == 1:
        tiene_visa = True
    else:
        tiene_visa = False


def leer_ciudades(archivo):
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        cuenta = 0
        for row in csv_reader:
            valor = cambiar_bool(row[2])
            ciudad = Ciudad(row[1], row[0], valor)
            ciudades[ciudad.codigo] = ciudad
            lista_ciudad.append(row[1])
            for i in grafo:
                i.append(0)
            grafo.append([0]*(len(grafo)+1))
            indice_ciudad[ciudad.codigo] = len(indice_ciudad)
            cuenta += 1
        print(f'Se agregaron {cuenta} ciudades')


def cambiar_bool(string):
    if string == "True":
        string = True
    else:
        string = False
    return string


def print_grafo(grafo):
    for v, i in indice_ciudad.items():
        print(v + ' ', end='')
        for j in range(len(grafo)):
            print(grafo[i][j], end='')
        print(' ')


def leer_rutas(archivo):
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        cuenta = 0
        for row in csv_reader:
            origen = row[0]
            destino = row[1]
            costo = row[2]
            grafo[indice_ciudad[origen]][indice_ciudad[destino]] = costo
            grafo[indice_ciudad[destino]][indice_ciudad[origen]] = costo
            cuenta += 1
        print(f'Se agregaron {cuenta} rutas')


menu()
