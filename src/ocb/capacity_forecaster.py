"""
Predictive Capacity Forecaster
Estimates future learning capacity to avoid collapse.
"""

class CapacityForecaster:
    def __init__(self, window: int = 5):
        self.window = window
        self.history = []

    def update(self, capacity_value: float):
        self.history.append(capacity_value)
        if len(self.history) > self.window:
            self.history.pop(0)

    def forecast(self) -> float:
        if not self.history:
            return 0.0
        return sum(self.history) / len(self.history)