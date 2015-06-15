class Data:
    def __init__(self):
        with open("data/places.txt", "r") as myfile:
            self.rawPlaces = myfile.read().replace('\n', '')

        with open("data/distances.txt", "r") as myfile:
            self.rawDistances = myfile.read()

        self.distances = []
        self.places = []

        self.extract_places()
        self.extract_distances()

    def get_distances(self):
        return self.distances

    def get_places(self):
        return self.places

    def extract_distances(self):
        self.distances = []
        distances_lines = self.rawDistances.split("\n")

        line_index = 0
        for distancesLine in distances_lines:
            distances = distancesLine.split(',')
            row_index = 0

            for distance in distances:
                self.distances.append({
                    "from": self.places[row_index],
                    "to": self.places[line_index],
                    "value": int(distance),
                    "weight": 0
                })
                row_index += 1

            line_index += 1

    def extract_places(self):
        self.places = self.rawPlaces.split(",")
        print(str(len(self.places)) + " places")
