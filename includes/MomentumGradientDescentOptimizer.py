from includes.Optimizer import Optimizer


class MomentumGradientDescentOptimizer(Optimizer):
    def __init__(self, label, number_of_steps, learning_rate, momentum=0.9):
        super().__init__(label, number_of_steps)

        self.set_learning_rate(learning_rate)
        self.set_momentum(momentum)

    def get_optimization_path_of_optimization_of_function_from_point(self, func, start) -> list[tuple]:
        ans = [start]

        past_updates = 0, 0

        for i in range(self.max_number_of_steps):
            current = ans[-1]
            dx, dy = func.derivative_at(current)
            upx, upy = - (1 - self.momentum) * dx + self.momentum * past_updates[0], - (
                    1 - self.momentum) * dy + self.momentum * past_updates[1]
            x, y = current[0] + self.learning_rate * upx, current[1] + self.learning_rate * upy
            past_updates = upx, upy
            ans.append((x, y))
            if func.is_approximation_close_enough((x, y)):
                break

        self.number_of_steps = len(ans) - 1

        return ans
