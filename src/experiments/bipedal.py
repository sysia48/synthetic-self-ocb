# experiments/bipedal.py

from synthetic_self import SyntheticSelf, Memory, Identity, Stability


class CapacityForecaster:
    def __init__(self):
        self.loads = []

    def update(self, load):
        self.loads.append(load)

    def capacity(self):
        return sum(self.loads) / len(self.loads) if self.loads else 0.0


# init system
memory = Memory()
identity = Identity()
stability = Stability()

agent = SyntheticSelf(identity, memory, stability)
capacity = CapacityForecaster()


# simulation loop
for step in range(5):
    state = {"step": step, "load": step * 0.15}
    output = agent.process(state)
    capacity.update(load=state["load"])


# results
print("last output:", output)
print("capacity:", capacity.capacity())