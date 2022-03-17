from Ciudad import Ciudad
import csv

grafo = []
ciudades = {}
indice_ciudad = {}
lista_ciudad = []

def leer_rutas(archivo, cortador):
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        cuenta = 0
        for row in csv_reader:
            #Se toma los codigos de las ciudades de origen destino y el costo entre ellos       para crear las rutas
            #Notese que en el enunciado pone que es el mismo precio para ambas direcciones      por lo que no es dirigido
            origen = row[0]
            destino = row[1]
            costo = row[2]
            ciudad_origen = ciudades[origen]
            ciudad_destino = ciudades[destino]
            visa_origen = ciudades[origen].visa
            visa_destino = ciudades[destino].visa
            if visa_origen == True or visa_destino == True:
                grafo[indice_ciudad[ciudad_origen]][indice_ciudad[ciudad_destino]] = int(costo) + cortador
                grafo[indice_ciudad[ciudad_destino]][indice_ciudad[ciudad_origen]] = int(costo) + cortador
            else:
                grafo[indice_ciudad[ciudad_origen]][indice_ciudad[ciudad_destino]] = int(costo)
                grafo[indice_ciudad[ciudad_destino]][indice_ciudad[ciudad_origen]] = int(costo)
            cuenta += 1
        print(f'Se agregaron {cuenta} rutas')

def leer_ciudades(archivo):
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        cuenta = 0
        #para cada sector separado por comas del archivo
        for row in csv_reader:
            # Crea una lista de booleanos que son verdaderos o falsos dependiendo de las ciudades que requieren Visa.
            # ciudades_que_requieren_visa.append(eval(row[2]))
            #Se crea una instancia con los valores adecuados
            ciudad = Ciudad(row[1], row[0], eval(row[2]))
            #Se almacena en el diccionario adecuado
            ciudades[ciudad.codigo] = ciudad
            lista_ciudad.append(row[1])
            for i in grafo:
                i.append(0)
            grafo.append([0] * (len(grafo) + 1))
            indice_ciudad[ciudad] = len(indice_ciudad)
            cuenta += 1
        print(f'Se agregaron {cuenta} ciudades')


def leerNodos(archivo):
    listaNombre = []
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            listaNombre.append(row[0])
    return listaNombre

def leerNodosSinVisa(archivo):
    listaNombre = []
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
          if(not(eval(row[2]))):
            listaNombre.append(row[0])
    print("nodos sin visa es: ",len(listaNombre))
    return listaNombre


def leerAristas(archivo):
    listaAristas = []
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            listaAristas.append(row)

    return listaAristas
