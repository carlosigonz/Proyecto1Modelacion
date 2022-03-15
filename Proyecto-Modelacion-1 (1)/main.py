
#Ciudades se cargan bien, lee que hay 20 rutas pero no lo carga tan bien
#Posibles errores: indice_ciudad mal creado, indice_ciudad mal leido, orden en que se agregan los ejes mal.
#codigo de grafos interpretado por https://youtu.be/HDUzBEG1GlA?t=387
import networkx as nx
import matplotlib.pyplot as plt
from archivo import *
import graphviz

#Donde se guarda el grafo
listaGrafo=[]
#Guarda el codigo de las ciudades como llave y el objeto como valor
ciudades = {}
#Guarda el codigo como llave y el numero de ciudades como ValueError
#posible error de que los indices no esten funcionando bien
indice_ciudad = {}


cortador = 0
#Clase para las ciudades con su nombre codigo y visa

def menu():

    tiene_visa = input(
        "Escriba el número según corresponda\n1.Tiene Visa\n2.No tiene Visa: ")

    while tiene_visa != "2" and tiene_visa !="1":
        tiene_visa = input("Insertó una opción inválida. Escriba el número según     corresponda\n1.Tiene Visa\n2.No tiene Visa: ")

    tiene_visa = int(tiene_visa)
    if tiene_visa == 1:
        tiene_visa = True
      
    else:
        tiene_visa = False
        contador = 999
  
	#Carga los vertices del grafo
    leer_ciudades("Datos Ciudades.csv")
   
	#Carga las rutas
    leer_rutas("Datos Rutas.csv",cortador,"Datos Ciudades.csv")
  
	#imprime el grafo
    print_grafo(grafo)
        
    print("Bienvenido a Metro Travel.")
  
    #Menú para recoger los datos del usuario
    ciudad_origen = input("Escriba el nombre de la ciudad origen\n")
    seguir = False
    while seguir == False:
        for i in lista_ciudad:
          if ciudad_origen.lower() == i.lower():
            seguir = True
            break
        if seguir == False:
            ciudad_origen = input("El nombre de la ciudad no es correcto, por favor escriba el nombre de la            ciudad origen\n")

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

    algoritmo = input("Elija el número según corresponda\n1.Costo mínimo\n2.Camino más corto: ")

    if algoritmo==1:
    #costo minimo(grafo)
      print("Aqui algoritmo")
    else:
      #Camino más corto(grafo)
      print("Aqui otro algoritmo")

    G=nx.Graph()
  
    G.add_nodes_from(["Caracas","Aruba","Bonaire","Curazao","San Martin","Santo Domingo",])

    G.add_edge("Caracas","Aruba")

    G.add_edge("Aruba","Bonaire")

    G.add_edge("Curazao","Caracas")

    G.add_edge("San Martin","Santo Domingo")

    G.add_edge("Santo Domingo","Caracas")

    G.add_edge("Bonaire","Caracas")

    plt.show()
    nx.draw(G)

    plt.savefig("networkx1.png")
    A = nx.nx_agraph.to_agraph(G)
    A.layout('dot')
    A.draw('salida.png') # guardar como png
 
  


def print_grafo(grafo):
  for v,i in indice_ciudad.items():
    print(v + ' ', end='') 
    for j in range(len(grafo)):
    #  Esto lo hago, pa divertirme, pa divertirme, pa divertirme
      print(grafo[i][j], end='')
    print(' ')


#Se corre el programa

menu()



  
