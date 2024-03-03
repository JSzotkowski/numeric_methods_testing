from includes.Optimizer import Optimizer


class GradientDescentOptimizer(Optimizer):
    def __init__(self, label, number_of_steps, learning_rate):
        super().__init__(label, number_of_steps)

        self.set_learning_rate(learning_rate)

    def get_optimization_path_of_optimization_of_function_from_point(self, func, start) -> list[tuple]:
        ans = [start]

        for i in range(self.max_number_of_steps):
            current = ans[-1]
            dx, dy = func.derivative_at(current)
            x, y = current[0] - self.learning_rate * dx, current[1] - self.learning_rate * dy
            ans.append((x, y))
            if func.is_approximation_close_enough((x, y)):
                break

        self.number_of_steps = len(ans) - 1

        return ans
