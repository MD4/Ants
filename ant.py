import copy
import random

class Ant:
    def __init__(self, graph, start_place):
        self.graph = graph
        self.place = start_place
        self.stack = []
        self.distance = 0

        self.places_to_go = copy.deepcopy(graph.get_nodes())
        self.places_to_go.remove(start_place)

    def pick_one(self, choices):
        def add_weight(x, y):
            return x + y['weight']

        weight_sum = reduce(add_weight, choices, 0)
        pick = int(round(random.random() * weight_sum))

        def pick_random_index():
            current_grade_sum = 0
            current_index = 0
            for choice in choices:
                current_grade_sum += choice['weight']
                if current_grade_sum >= pick:
                    return current_index
                current_index += 1
            return -1

        random_index = pick_random_index()
        return choices[random_index]

    def pick_place(self):
        choices = []
        for place in self.places_to_go:
            weight = self.graph.get_weight(self.place, place) + 1
            choices.append({
                'place': place,
                'weight': weight
            })
        return self.pick_one(choices)['place']

    def run(self):
        while len(self.places_to_go):
            self.step()
        return self.distance

    def pheromonize(self):
        for path in self.stack:
            self.graph.update_weight(path['from'], path['to'])

    def step(self):
        new_place = self.pick_place()
        self.stack.append({
            'from': self.place,
            'to': new_place
        })
        self.distance += self.graph.get_distance(self.place, new_place)
        self.place = new_place
        self.places_to_go.remove(self.place)
