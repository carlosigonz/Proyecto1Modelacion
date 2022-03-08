import csv

grafo=[]
ciudades = {}
indice_ciudad = {}

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

def leer_ciudades(archivo):
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        cuenta = 0
        for row in csv_reader:
            valor = cambiar_bool(row[2])
            ciudad = Ciudad(row[1],row[0],valor)
            ciudades[ciudad.codigo] = ciudad
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
    for v,i in indice_ciudad.items():
        print(v + ' ', end='')
        for j in range(len(grafo)):
            print(grafo[i][j]+" ", end='')
        print(' ')

def leer_rutas(archivo):
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        cuenta = 0
        for row in csv_reader:
            origen = row[0]
            destino = row[1]
            costo = row[2]
            print(origen)
            print(destino)
            print(costo)
            grafo[indice_ciudad[origen]][indice_ciudad[destino]] = costo
            grafo[indice_ciudad[destino]][indice_ciudad[origen]] = costo
            cuenta += 1
        print(f'Se agregaron {cuenta} rutas')

menu()

