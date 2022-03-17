# codigo de grafos interpretado por https://youtu.be/HDUzBEG1GlA?t=387
import networkx as nx
import matplotlib.pyplot as plt
from archivo import *

cortador = 0


def menu():
    print("Bienvenido a Metro Travel.")
    cortador, visa_pasajero = verificador_de_visa()
    # Carga los vertices del grafo
    leer_ciudades("Datos Ciudades.csv")
    # Carga las rutas
    leer_rutas("Datos Rutas.csv", cortador)
    # Menú para recoger los datos del usuario
    ciudad_origen = definidor_ciudad_origen(visa_pasajero)
    ciudad_destino = definidor_ciudad_destino(visa_pasajero, ciudad_origen)
    definidor_algoritmo(grafo, ciudad_origen, ciudad_destino, visa_pasajero)


def verificador_de_visa():
    tiene_visa = input(
        "Escriba el número según corresponda\n1.Tiene Visa\n2.No tiene Visa: ")
    while tiene_visa != "2" and tiene_visa != "1":
        tiene_visa = input(
            "Insertó una opción inválida. Escriba el número según corresponda\n1.Tiene Visa\n2.No tiene Visa: "
        )
    if tiene_visa == "1":
        cortador = 0
        visa_pasajero = True
    else:
        cortador = 9999
        visa_pasajero = False
    return cortador, visa_pasajero


def definidor_ciudad_origen(visa_pasajero):
    ciudad_origen = input(
        "Escriba el nombre o el código de la ciudad origen\n")
    seguir = False
    detener_por_falta_de_visa = False
    while seguir == False:
        for i in ciudades:
            if ciudad_origen.upper() == i or ciudad_origen.lower(
            ) == ciudades[i].nombre.lower():
                nombre_origen = ciudades[i].nombre
                codigo_origen = ciudades[i].codigo
                print(
                    f'Ciudad de Origen: {nombre_origen} \nCódigo Aeropuerto: {codigo_origen}'
                )
                if visa_pasajero == False and ciudades[i].visa == True:
                    print(
                        "No cuenta con la visa para iniciar en esta ciudad. Por favor incerte una ciudad origen que no requiera visa: "
                    )
                    ciudad_origen = input()
                    detener_por_falta_de_visa = True

                else:
                    ciudad_origen = ciudades[i]
                    seguir = True
                    break
        if seguir == False and detener_por_falta_de_visa == False:
            ciudad_origen = input(
                "El nombre de la ciudad no es correcto, por favor escriba el nombre o el código de la ciudad origen\n"
            )
    return ciudad_origen


def definidor_ciudad_destino(visa_pasajero, ciudad_origen):
    ciudad_destino = input(
        "Escriba el nombre o el código de la ciudad destino\n")
    seguir = False
    detener_por_falta_de_visa = False
    detener_por_colocar_ciudad_origen_igual_a_la_ciudad_destino = False
    while seguir == False:
        for i in ciudades:
            if ciudad_destino.upper() == i or ciudad_destino.lower(
            ) == ciudades[i].nombre.lower():
                if ciudad_origen == ciudades[i]:
                    print(
                        "El destino no puede ser igual al origen. Por favor elija un destino distinto al origen: "
                    )
                    ciudad_destino = input()
                    detener_por_colocar_ciudad_origen_igual_a_la_ciudad_destino = True

                else:
                    nombre_destino = ciudades[i].nombre
                    codigo_destino = ciudades[i].codigo
                    print(
                        f'Ciudad de Origen: {nombre_destino} \nCódigo Aeropuerto: {codigo_destino}'
                    )
                    if visa_pasajero == False and ciudades[i].visa == True:
                        print(
                            "No cuenta con la visa para terminar en esta ciudad. Por favor elija un destino que no requiera visa: "
                        )
                        ciudad_destino = input()
                        detener_por_falta_de_visa = True

                    else:
                        ciudad_destino = ciudades[i]
                        seguir = True

                        break
        if seguir == False and detener_por_falta_de_visa == False and detener_por_colocar_ciudad_origen_igual_a_la_ciudad_destino == False:
            ciudad_destino = input(
                "El nombre de la ciudad no es correcto, por favor escriba el nombre de la ciudad destino\n"
            )
    return ciudad_destino


def print_grafo(grafo):
    for v, i in indice_ciudad.items():
        print(v + ' ', end='')
        for j in range(len(grafo)):
            print(grafo[i][j], end='')
        print(' ')


def print_grafo2(grafo):
    for i in range(len(grafo)):
        print(grafo[i])
        print("\n")


def definidor_algoritmo(grafo, ciudad_origen, ciudad_destino, visa_pasajero):
    algoritmo = input(
        "Elija el método de busqueda de rutas que desee\n1.Costo mínimo\n2.Número segmentos mínimo: "
    )
    while algoritmo != "1" and algoritmo != "2":
        algoritmo = input(
            "La opción que eligió es inválida. Elija el número según corresponda\n1.Costo mínimo\n2.Camino más corto: "
        )
    algoritmo = int(algoritmo)
    if algoritmo == 1:
        costo_minimo(grafo, ciudad_origen, ciudad_destino, visa_pasajero)
    else:
        camino_corto(ciudad_origen, ciudad_destino, visa_pasajero)

    return algoritmo


def camino_corto(origen, destino, visa):
    if visa:
        
        G = nx.Graph()
        G.add_nodes_from(leerNodos("Datos Ciudades.csv"))
        listaArista = leerAristas("Datos Rutas.csv")
        for arista in listaArista:
            G.add_edge(arista[0], arista[1], weight=int(arista[2]))
        pos = nx.planar_layout(G)
        dj = nx.shortest_path(G, origen.codigo, destino.codigo, weight='weight')
        dj_edges = [(dj[i], dj[i + 1]) for i in range(len(dj) - 1)]
        edge_color_list = ["black"] * len(G.edges)
        for i, edge in enumerate(G.edges()):
            if edge in dj_edges or (edge[1], edge[0]) in dj_edges:
                edge_color_list[i] = 'red'
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw(G, pos, with_labels=True, edge_color=edge_color_list)
        print(f'\nRuta Final: \n')
        for i in dj:
            print(f'{i}', end=' -> ')
       
        H= G.subgraph(dj)
        peso = nx.get_edge_attributes(H, 'weight')
        # print(peso)
        costos = peso.values()
        costo_total = sum(costos)
        print("Costo total: $",costo_total)
      
        plt.show()
    else:
        G = nx.Graph()
        G.add_nodes_from(leerNodosSinVisa("Datos Ciudades.csv"))
        listaArista = leerAristas("Datos Ciudades visa.csv")
        for arista in listaArista:
            G.add_edge(arista[0], arista[1], weight=int(arista[2]))

        pos = nx.planar_layout(G)
        dj = nx.shortest_path(G, origen.codigo, destino.codigo, weight='weight')
        dj_edges = [(dj[i], dj[i + 1]) for i in range(len(dj) - 1)]
        edge_color_list = ["black"] * len(G.edges)
        for i, edge in enumerate(G.edges()):
            if edge in dj_edges or (edge[1], edge[0]) in dj_edges:
                edge_color_list[i] = 'red'
        labels = nx.get_edge_attributes(G, 'weight')

        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw(G, pos, with_labels=True, edge_color=edge_color_list)
        print(f'\nRuta Final: \n')
        for i in dj:
            print(f'{i}', end=' -> ')
        H= G.subgraph(dj)
        peso = nx.get_edge_attributes(H, 'weight')
        # print(peso)
        costos = peso.values()
        costo_total = sum(costos)
        print("Costo total: $",costo_total)
        plt.show()

      


def costo_minimo(grafo, origen, destino, visa_pasajero):
    padres = [-1] * len(grafo)
    costos = [float("inf") for x in range(len(grafo))]
    visitados = [False for x in range(len(grafo))]
    indice_inicio = indice_ciudad[origen]
    indice_final = indice_ciudad[destino]
    costos[indice_inicio] = 0
    while True:
        distancia_mas_corta = float("inf")
        indice_mas_corto = -1
        for i in range(len(grafo)):
            if costos[i] < distancia_mas_corta and not visitados[i]:
                distancia_mas_corta = costos[i]
                indice_mas_corto = i
        # print("Visitando " + str(indice_mas_corto) + " Distancia: " + str(distancia_mas_corta))

        if indice_mas_corto == -1:
            # print("Visitados todos")
            break
        for i in range(len(grafo[indice_mas_corto])):
            if grafo[indice_mas_corto][i] != 0 and costos[
                    i] > costos[indice_mas_corto] + grafo[indice_mas_corto][i]:
                costos[
                    i] = costos[indice_mas_corto] + grafo[indice_mas_corto][i]
                padres[i] = indice_mas_corto
                # print("actualizando distancia de la ciudad "+ str(i) +" hacia " + str(costos[i]))
        visitados[indice_mas_corto] = True
        # print("Nodos visitados: " + str(visitados))
        # print("Actualmente distancias mas cortas: " + str(costos))
        if visitados[indice_final] == True:
            break
    indice_rutas = hacer_ruta(padres, indice_final)
    ruta_final = []
    for i in indice_rutas:
        ruta_final.append(lista_ciudad[i])
    costo_final = costos[indice_final]
    costo_final = str(costo_final)
    print(f'\nRuta Final: \n')
    for i in ruta_final:
        print(f'{i}', end=' -> ')
    print(
        f'\nCosto Total Viaje {origen.nombre}({origen.codigo}) -> {destino.nombre}({destino.codigo}):\n ${costo_final}'
    )
    graficarDijkstra(origen.codigo, destino.codigo, visa_pasajero)


indice_rutas = []


def hacer_ruta(padres, predecesor):
    if padres[predecesor] == -1:
        indice_rutas.append(predecesor)
        return
    hacer_ruta(padres, padres[predecesor])
    indice_rutas.append(predecesor)
    return indice_rutas


def graficarDijkstra(origen, destino, visa):
    if (visa):
        # print("ESTOY ENTRANDO A VISA DIJKSTRA")
        G = nx.Graph()
        G.add_nodes_from(leerNodos("Datos Ciudades.csv"))
        listaArista = leerAristas("Datos Rutas.csv")
        for arista in listaArista:
            G.add_edge(arista[0], arista[1], weight=int(arista[2]))
        pos = nx.planar_layout(G)
        dj = nx.dijkstra_path(G, origen, destino, weight='weight')
        dj_edges = [(dj[i], dj[i + 1]) for i in range(len(dj) - 1)]
        edge_color_list = ["black"] * len(G.edges)
        for i, edge in enumerate(G.edges()):
            if edge in dj_edges or (edge[1], edge[0]) in dj_edges:
                edge_color_list[i] = 'red'
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw(G, pos, with_labels=True, edge_color=edge_color_list)
        plt.show()

    else:
        # print("ESTOY ENTRANDO A sin visa DIJKSTRA")
        G = nx.Graph()
        G.add_nodes_from(leerNodosSinVisa("Datos Ciudades.csv"))
        listaArista = leerAristas("Datos Ciudades visa.csv")
        for arista in listaArista:
            G.add_edge(arista[0], arista[1], weight=int(arista[2]))

        #nx.draw(G,pos, with_labels = True)
        #nx.draw_networkx_nodes(G,pos,node_size=50,label=leerNodos("Datos Ciudades.csv"))
        pos = nx.planar_layout(G)
        dj = nx.dijkstra_path(G, origen, destino, weight='weight')
        dj_edges = [(dj[i], dj[i + 1]) for i in range(len(dj) - 1)]
        edge_color_list = ["black"] * len(G.edges)
        for i, edge in enumerate(G.edges()):
            if edge in dj_edges or (edge[1], edge[0]) in dj_edges:
                edge_color_list[i] = 'red'
        labels = nx.get_edge_attributes(G, 'weight')
        #nx.draw(G,pos, with_labels = True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw(G, pos, with_labels=True, edge_color=edge_color_list)
        #nx.draw_networkx_edges(G, pos,)
        plt.show()



menu()
