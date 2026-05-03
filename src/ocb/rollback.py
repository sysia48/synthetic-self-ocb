class RollbackManager:
    def __init__(self):
        self.history = []

    def save(self, state):
        self.history.append(state)