from includes.Optimizer import Optimizer


class AdaptiveGradientOptimizer(Optimizer):
    def __init__(self, label, number_of_steps, learning_rate):
        super().__init__(label, number_of_steps)

        self.set_learning_rate(learning_rate)

    def get_optimization_path_of_optimization_of_function_from_point(self, func, start) -> list[tuple]:
        # eps = 0.00000001
        eps = 1
        ans = [start]

        g_sum_x, g_sum_y = 0, 0

        for i in range(self.max_number_of_steps):
            current = ans[-1]
            dx, dy = func.derivative_at(current)
            g_sum_x, g_sum_y = g_sum_x + dx ** 2, g_sum_y + dy ** 2
            vx, vy = (g_sum_x + eps) ** 0.5, (g_sum_y + eps) ** 0.5
            x, y = current[0] - self.learning_rate * dx / vx, current[1] - self.learning_rate * dy / vy
            ans.append((x, y))
            if func.is_approximation_close_enough((x, y)):
                break

        self.number_of_steps = len(ans) - 1

        return ans
