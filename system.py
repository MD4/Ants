from ant import Ant

class AntSystem:
    def __init__(self, graph, ants_count):
        self.best_distance = float("inf")
        self.graph = graph
        self.ants_count = ants_count

    def run(self, start_node_name):
        self.best_distance = float("inf")
        for step in range(0, self.ants_count):
            self.step(start_node_name)

    def step(self, start_node_name):
        ant = Ant(self.graph, start_node_name)
        distance = ant.run()
        if distance < self.best_distance:
            ant.pheromonize()
            self.best_distance = distance
