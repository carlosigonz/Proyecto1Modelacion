from Ciudad import Ciudad
import csv
grafo=[]
rutas=[]
ciudades = {}
indice_ciudad = {}
lista_ciudad = []
ciudades_que_requieren_visa = []



def leer_rutas(archivo,cortador,archivo_ciudad):

    with open(archivo_ciudad) as csv_file:
      csv_reader = csv.reader(csv_file,delimiter=',')
      for row in csv_reader:
        ciudades_que_requieren_visa.append(eval(row[2]))
      
    with open(archivo) as csv_file:
      csv_reader = csv.reader(csv_file,delimiter=',')
      cuenta = 0
      
      for row in csv_reader:
  	#Se toma los codigos de las ciudades de origen destino y el costo entre ellos       para crear las rutas
  	#Notese que en el enunciado pone que es el mismo precio para ambas direcciones      por lo que no es dirigido
        origen = row[0]
        destino = row[1]
        costo = row[2]

        for verifica_si_requiere_visa in ciudades_que_requieren_visa:
          if ciudades_que_requieren_visa == True:
            grafo[indice_ciudad[origen]][indice_ciudad[destino]] = int(costo) + cortador
            grafo[indice_ciudad[destino]][indice_ciudad[origen]] = int(costo) + cortador 
          else:
            grafo[indice_ciudad[origen]][indice_ciudad[destino]] = int(costo)
            grafo[indice_ciudad[destino]][indice_ciudad[origen]] = int(costo)
          
             
              

              
             


        
        

  
      
     # for row in cvs_reader:
       # tiene_visa = eval(row[2])
       # if tiene_visa == True:
       #   grafo[indice_ciudad[origen]][indice_ciudad[destino]] = costo + cortador
        #  grafo[indice_ciudad[destino]][indice_ciudad[origen]] = costo + cortador
       # else:
       #   grafo[indice_ciudad[origen]][indice_ciudad[destino]] = costo 
       #   grafo[indice_ciudad[destino]][indice_ciudad[origen]] = costo
      



      
      cuenta += 1
      print(f'Se agregaron {cuenta} rutas')

def leer_ciudades(archivo):
    with open(archivo) as csv_file:
      csv_reader = csv.reader(csv_file,delimiter=',')
      cuenta = 0
      
  		#para cada sector separado por comas del archivo
      for row in csv_reader:
  			#Se crea una instancia con los valores adecuados
        ciudad = Ciudad(row[1],row[0],eval(row[2]))
        #Se almacena en el diccionario adecuado
        ciudades[ciudad.codigo] = ciudad
        lista_ciudad.append(row[1])
        for i in grafo:
            i.append(0)
        grafo.append([0]*(len(grafo)+1))
  			#posible error almacenando o leyendo
        indice_ciudad[ciudad.codigo] = len(indice_ciudad)
        cuenta += 1
      print(f'Se agregaron {cuenta} ciudades')

