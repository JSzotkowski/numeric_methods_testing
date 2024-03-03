class Optimizer:
    def __init__(self, label, number_of_steps):
        self.label = label
        self.max_number_of_steps = number_of_steps
        self.number_of_steps = -1

        self.learning_rate = None
        self.momentum = None
        self.beta1 = None
        self.beta2 = None

    def get_label(self):
        return self.label

    def set_learning_rate(self, value):
        self.learning_rate = value

    def set_momentum(self, value):
        self.momentum = value

    def set_beta1(self, value):
        self.beta1 = value

    def set_beta2(self, value):
        self.beta2 = value

    def get_json_dict(self):
        ans = dict()

        ans["label"] = self.label
        ans["lr"] = self.learning_rate if self.learning_rate is not None else "-"
        ans["mtm"] = self.momentum if self.momentum is not None else "-"
        ans["beta1"] = self.beta1 if self.beta1 is not None else "-"
        ans["beta2"] = self.beta2 if self.beta2 is not None else "-"

        return ans

    def get_optimization_path_of_optimization_of_function_from_point(self, function, start) -> list[tuple]:
        raise Exception("Abstract method not implemented!")
