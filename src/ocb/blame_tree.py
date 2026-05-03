class BlameTree:
    def __init__(self):
        self.log = []

    def assign(self, action, reward):
        self.log.append((action, reward))