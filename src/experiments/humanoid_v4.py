# experiments/humanoid_v4.py

from synthetic_self import SyntheticSelf, Memory, Identity, Stability


class CapacityForecaster:
    def __init__(self):
        self.loads = []

    def update(self, load):
        self.loads.append(load)

    def capacity(self):
        return sum(self.loads) / len(self.loads) if self.loads else 0.0


class BlameTree:
    def __init__(self):
        self.log = []

    def assign(self, action, reward):
        self.log.append((action, reward))


class RollbackManager:
    def __init__(self):
        self.history = []

    def save(self, state):
        self.history.append(state)


# init system
memory = Memory()
identity = Identity()
stability = Stability()

agent = SyntheticSelf(identity, memory, stability)

capacity = CapacityForecaster()
blame = BlameTree()
rollback = RollbackManager()


# single step simulation
state = {"reward": 1.0, "loss": 0.2}

output = agent.process(state)
blame.assign("action_1", state["reward"])
capacity.update(load=0.3)
rollback.save(state)


# results
print("last output:", output)
print("capacity:", capacity.capacity())
print("blame log:", blame.log)