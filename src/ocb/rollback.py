"""
Surgical Rollback
Allows controlled rollback to last stable state.
"""

class RollbackManager:
    def __init__(self):
        self.checkpoints = []

    def save(self, state):
        self.checkpoints.append(state)

    def rollback(self):
        if not self.checkpoints:
            return None
        return self.checkpoints.pop()