import numpy as np


class Matrix:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.name, self.instance_size, self.matrix = self.load_data()

    def load_data(self):
        f = open(self.file_name, "r")
        name = f.readline()
        instance_size = int(f.readline())
        cities = []
        for x in f:
            row = x.split()
            for i in range(len(row)):
                row[i] = int(row[i])
            cities.append(row)
        cities = np.asarray(cities)
        return name, instance_size, cities

    def get_matrix(self):
        return self.matrix

    def get_name(self):
        return self.name

    def get_size(self):
        return self.instance_size
