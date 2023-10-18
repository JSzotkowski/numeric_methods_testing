from json import dumps


class OptimizationRecord:
    def __init__(self, optimizer, func, starting_point, optimizer_path=None):
        self.label = f'{optimizer.get_label()} on {func.get_label()} from {starting_point}'
        self.func = func
        self.optimizer = optimizer
        self.starting_point = starting_point
        self.optimizer_path = optimizer_path if optimizer_path is not None else []

    def get_label(self):
        return self.label

    def get_json_dict(self):
        ans = dict()

        ans["label"] = self.label
        ans["func"] = self.func.get_json_dict()
        ans["optimizer"] = self.optimizer.get_json_dict()
        ans["optimizer_path"] = self.optimizer_path

        return ans

    def optimize(self):
        self.optimizer_path = self.optimizer.get_optimization_path_of_optimization_of_function_from_point(
            self.func,
            self.starting_point
        )

    def append_step(self, coordinates):
        self.optimizer_path.append(coordinates)

    def __getitem__(self, item):
        return self.optimizer_path[item]

    def __setitem__(self, key, value):
        self.optimizer_path[key] = value
