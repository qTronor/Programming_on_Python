class main:

    def __init__(self):
        self.state = "A"
        self._graph = {
            ("A", "visit"): ("B", 0),
            ("A", "crack"): ("D", 1),
            ("B", "crack"): ("C", 2),
            ("C", "crack"): ("D", 3),
            ("D", "visit"): ("E", 4),
            ("E", "crack"): ("F", 5),
            ("F", "visit"): ("B", 7),
            ("F", "crack"): ("G", 6),
            ("G", "crack"): ("C", 8),
            ("G", "visit"): ("E", 9)
        }

    def crack(self):
        self.state, ret_value = self._graph[(self.state, "crack")]
        return ret_value

    def visit(self):
        self.state, ret_value = self._graph[(self.state, "visit")]
        return ret_value


o = main()
print(o.crack())  # 1
print(o.visit())  # 4
print(o.crack())  # 5
print(o.crack())  # 6
print(o.visit())  # 9
print(o.crack())  # 5
print(o.crack())  # 6
print(o.crack())  # 8
print(o.crack())  # 3
print(o.visit())  # 4
print(o.crack())  # 5
print(o.visit())  # 7
print(o.crack())  # 2
print(o.crack())  # 3
