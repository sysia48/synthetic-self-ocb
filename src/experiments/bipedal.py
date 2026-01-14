from ocb.synthetic_self import SyntheticSelf
from ocb.capacity_forecaster import CapacityForecaster

agent = SyntheticSelf(identity_id="bipedal-agent")
capacity = CapacityForecaster()

for step in range(5):
    state = {"step": step, "load": step * 0.15}
    agent.observe(state)
    capacity.update(load=state["load"])

print("continuity:", agent.continuity())
print("capacity:", capacity.capacity())