from copy import deepcopy

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def get_nodes(self):
        return self.nodes

    def get_edge(self, from_name, to_name):
        return filter(lambda x: x['from'] == from_name and x['to'] == to_name, self.edges)[0]

    def get_distance(self, from_name, to_name):
        return self.get_edge(from_name, to_name)['value']

    def get_weight(self, from_name, to_name):
        return self.get_edge(from_name, to_name)['weight']

    def update_weight(self, from_name, to_name):
        self.get_edge(from_name, to_name)['weight'] += 1
        self.get_edge(to_name, from_name)['weight'] += 1

    def get_best_path(self, start_place):
        node = start_place
        nodes = deepcopy(self.nodes)
        nodes.remove(node)
        path = [start_place]
        distance = 0
        while len(nodes) > 0:
            best_node = None
            for to_node in nodes:
                if best_node is None or self.get_weight(node, best_node) < self.get_weight(node, to_node):
                    best_node = to_node
            distance += self.get_distance(node, best_node)
            path.append(best_node)
            node = best_node
            nodes.remove(node)
        return {
            'path': path,
            'distance': distance
        }

    def to_string(self):
        print(self.edges)