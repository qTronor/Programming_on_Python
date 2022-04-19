class main:

    def __init__(self):
        self.state = "A"
        self._graph = {
            ("A", "reset"): ('B', 0),
            ("A", "wreck"): ('C', 1),
            ("A", "push"): ('A', 2),
            ("B", "wreck"): ('C', 3),
            ("B", "push"): ('F', 4),
            ("C", "reset"): ('D', 5),
            ("C", "wreck"): ('F', 6),
            ("D", "push"): ('E', 7),
            ("E", "reset"): ('F', 8),
            ("F", "wreck"): ('G', 9)
        }

    def push(self):
        self.state, ret_value = self._graph[(self.state, "push")]
        return ret_value

    def reset(self):
        self.state, ret_value = self._graph[(self.state, "reset")]
        return ret_value

    def wreck(self):
        self.state, ret_value = self._graph[(self.state, "wreck")]
        return ret_value
