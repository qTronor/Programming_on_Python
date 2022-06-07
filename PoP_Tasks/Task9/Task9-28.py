class main:

    def __init__(self):
        self.state = "A"
        self._graph = {
            ("A", "model"): ("B", 0),
            ("B", "slog"): ("C", 1),
            ("B", "model"): ("F", 2),
            ("C", "model"): ("D", 3),
            ("C", "slog"): ("C", 4),
            ("D", "sort"): ("E", 5),
            ("E", "model"): ("F", 6),
            ("E", "sort"): ("E", 7),
            ("F", "slog"): ("G", 8),
            ("G", "model"): ("A", 9)
        }

    def slog(self):
        self.state, ret_value = self._graph[(self.state, "slog")]
        return ret_value

    def model(self):
        self.state, ret_value = self._graph[(self.state, "model")]
        return ret_value

    def sort(self):
        self.state, ret_value = self._graph[(self.state, "sort")]
        return ret_value


o = main()
print(o.model()) # 0
print(o.sort()) # KeyError
print(o.slog()) # 1
print(o.model()) # 3
print(o.sort()) # 5
print(o.sort())# 7
print(o.model()) # 6
print(o.slog()) # 8
print(o.model()) # 9
print(o.slog()) # 4
print(o.model()) # 3
print(o.sort()) # 5
print(o.model())