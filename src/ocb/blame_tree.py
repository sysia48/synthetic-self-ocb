"""
Outcome-Centric Blame Tree
Non-vanishing responsibility assignment.
"""

class BlameNode:
    def __init__(self, action, outcome):
        self.action = action
        self.outcome = outcome
        self.children = []

    def add_child(self, node):
        self.children.append(node)


class BlameTree:
    def __init__(self):
        self.root = None

    def assign(self, action, outcome):
        node = BlameNode(action, outcome)
        if self.root is None:
            self.root = node
        else:
            self.root.add_child(node)