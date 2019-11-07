class TSP:
    def __init__(self, path: list, cost: int):
        self.path = path
        self.cost = cost

    def get_path(self):
        return self.path

    def set_path(self, path: list):
        self.path = path.copy()
        self.path.insert(0, 0)
        self.path.append(0)

    def get_cost(self):
        return self.cost

    def set_cost(self, cost: int):
        self.cost = cost

    def show_result(self):
        print("Cost: ", self.cost)
        path = self.path.copy()
        for city in range(len(path)):
            path[city] = str(path[city])
        print(' -> '.join(path))