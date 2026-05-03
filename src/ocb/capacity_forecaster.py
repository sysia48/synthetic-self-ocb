class CapacityForecaster:
    def __init__(self):
        self.loads = []

    def update(self, load):
        self.loads.append(load)

    def capacity(self):
        return sum(self.loads) / len(self.loads) if self.loads else 0.0