from includes.Optimizer import Optimizer


class AdaptiveMomentEstimationOptimizer(Optimizer):
    def __init__(self, label, number_of_steps, learning_rate, beta1=0.9, beta2=0.999):
        super().__init__(label, number_of_steps)

        self.set_learning_rate(learning_rate)
        self.set_beta1(beta1)
        self.set_beta2(beta2)

    def get_optimization_path_of_optimization_of_function_from_point(self, func, start) -> list[tuple]:
        # eps = 0.00000001
        eps = 1
        ans = [start]

        mx, my = 0, 0
        vx, vy = 0, 0

        for i in range(self.max_number_of_steps):
            current = ans[-1]
            dx, dy = func.derivative_at(current)

            mx, my = (1 - self.beta1) * dx + self.beta1 * mx, (1 - self.beta1) * dy + self.beta1 * my
            vx, vy = ((1 - self.beta2) * (dx ** 2) + self.beta2 * vx) ** 0.5, (
                    (1 - self.beta2) * (dy ** 2) + self.beta2 * vy) ** 0.5

            x, y = current[0] - self.learning_rate * mx / (vx + eps) * ((1 - self.beta2) ** 0.5) / (1 - self.beta1), \
                   current[1] - self.learning_rate * my / (vy + eps) * ((1 - self.beta2) ** 0.5) / (1 - self.beta1)
            ans.append((x, y))
            if func.is_approximation_close_enough((x, y)):
                break

        self.number_of_steps = len(ans) - 1

        return ans
