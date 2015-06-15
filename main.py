from data import Data
from graph import Graph
from system import AntSystem

data = Data()

places = data.get_places()
edges = data.get_distances()

graph = Graph(places, edges)
system = AntSystem(graph, 100)

system.run('LE LIEU UNIQUE')

graph.to_string()

result = graph.get_best_path('LE LIEU UNIQUE')

print(result['path'])
print(result['distance'])
