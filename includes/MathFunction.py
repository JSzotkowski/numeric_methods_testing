class MathFunction:
    def __init__(self, label, func, derivative, desired_minimum):
        self.label = label
        self.func = func
        self.derivative = derivative

        self.desired_minimum = desired_minimum

        self.commentary = None

    def get_label(self):
        return self.label

    def set_commentary(self, value):
        self.commentary = value

    def evaluate(self, value):
        return self.func(*value)

    def derivative_at(self, value):
        return self.derivative(*value)

    def get_json_dict(self):
        ans = dict()

        ans["label"] = self.label
        ans["commentary"] = self.commentary if self.commentary is not None else "-"
        ans["desired_minimum"] = self.desired_minimum

        return ans


if __name__ == '__main__':
    quadratic_function = MathFunction("Kvadratická funkce f(x) = x^2", lambda t: t ** 2 + t + 1, lambda t: 2 * t + 1,
                                      [-2, 0, 1])

    for x in range(-5, 5, 1):
        assert quadratic_function.evaluate([x]) == x ** 2 + x + 1
        assert quadratic_function.derivative_at([x]) == 2 * x + 1

    ans = {"label": "Kvadratická funkce f(x) = x^2", "commentary": "-"}

    assert quadratic_function.get_json_dict() == ans

    ans["commentary"] = "Nádherná, viďte!"
    quadratic_function.set_commentary("Nádherná, viďte!")

    assert quadratic_function.get_json_dict() == ans
