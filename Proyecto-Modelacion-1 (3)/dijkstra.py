import sys
from heapq import heapify, heappush, heappop

def main():

    def dijkstra(graph, start, goal):
        shortest_distance = {}
        track_predecessor = {}
        unseenNodes = graph
        infinity = 99999
        track_path = []

        for node in unseenNodes:
            shortest_distance[node] = infinity
        shortest_distance[start] = 0

        while unseenNodes:

            min_distance_node = None

            for node in unseenNodes:
                if min_distance_node is None:
                    min_distance_node = node
                elif shortest_distance[node] < shortest_distance[min_distance_node]:
                    min_distance_node = node

            path_options = graph[min_distance_node].items()

            for child_node, weight in path_options:
                if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                    shortest_distance[child_node] = weight+shortest_distance[min_distance_node]
                    track_predecessor[child_node] = min_distance_node

            unseenNodes.pop(min_distance_node)

        currentNode = goal

        while currentNode != start:
            try:
                track_path.insert(0, currentNode)
                currentNode = track_predecessor[currentNode]

            except KeyError:
                print("Path is not reachable")
                break

        track_path.insert(0,start)

        if shortest_distance[goal] != infinity:
            print("Shortest distance is " + str(shortest_distance[goal]))
            print("Optimal path is " + str(track_path))
        

    grafo = {
        'A': {'B': 40, 'D': 35, 'C': 60, 'F': 180, 'H': 150, 'I': 180},
        'B': {'A': 40, 'D': 15, 'C': 15, 'E': 85},
        'C': {'A': 60, 'B': 15, 'D': 15},
        'D': {'A': 35, 'B': 15, 'C': 15, 'E': 80},
        'E': {'B': 85, 'D': 80, 'F': 50, 'G': 45, 'H': 90, 'I': 70, 'K': 100},
        'F': {'A': 180, 'E': 50},
        'G': {'E': 45, 'K': 80},
        'H': {'A': 150, 'E': 90, 'I': 35, 'J': 75, 'K': 80},
        'I': {'A': 180, 'E': 70, 'H': 35},
        'J': {'H': 75},
        'K': {'E': 100, 'H': 80, 'G': 80}
    }

    origen = 'A'
    destino = 'J'
    dijkstra(grafo, origen, destino)

main()