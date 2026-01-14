from ocb.synthetic_self import SyntheticSelf
from ocb.blame_tree import BlameTree
from ocb.capacity_forecaster import CapacityForecaster
from ocb.rollback import RollbackManager

self_model = SyntheticSelf(identity_id="agent-001")
blame = BlameTree()
capacity = CapacityForecaster()
rollback = RollbackManager()

state = {"reward": 1.0, "loss": 0.2}

self_model.observe(state)
blame.assign("action_1", state["reward"])
capacity.update(load=0.3)
rollback.save(state)

print("continuity:", self_model.continuity())
print("capacity:", capacity.capacity())