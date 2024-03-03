import numpy as np

from includes.Optimizer import Optimizer


class NelderMeadOptimizer(Optimizer):
    def __init__(self, label, number_of_steps, learning_rate):
        super().__init__(label, number_of_steps)

        self.set_learning_rate(learning_rate)

    def get_optimization_path_of_optimization_of_function_from_point(self, func, start) -> list[tuple]:
        ans = []

        alpha, gamma, ro, sigma = 1, 2, 1 / 2, 1 / 2
        n = len(start)
        centroid = np.asarray(start).reshape((n, 1))
        simplex = self.get_initial_simplex(centroid, n)
        flag = False

        for _ in range(self.max_number_of_steps):
            simplex.sort(key=lambda k: func.evaluate(k))
            centroid = self.get_centroid_of_a_simplex(simplex[:-1])
            ans.append(tuple([row[0] for row in self.get_centroid_of_a_simplex(simplex)]))
            if func.is_approximation_close_enough(centroid):
                flag = True
                break

            reflected = self.get_reflected_point(centroid, simplex[-1], alpha)

            f1, fr, fn = func.evaluate(simplex[0]), func.evaluate(reflected), func.evaluate(simplex[-2])
            if f1 <= fr < fn:
                self.replace_worst_point_in_simplex(simplex, reflected)
                continue
            if fr < f1:
                expanded = self.get_expanded_point(centroid, reflected, gamma)
                fe = func.evaluate(expanded)
                if fe < fr:
                    simplex.append(expanded)
                    continue
                self.replace_worst_point_in_simplex(simplex, reflected)
                continue
            fn1 = func.evaluate(simplex[-1])
            if fr < fn1:
                contracted = self.get_contracted_point_on_the_outside(centroid, reflected, ro)
                fc = func.evaluate(contracted)
                if fc < fr:
                    self.replace_worst_point_in_simplex(simplex, contracted)
                    continue
            contracted = self.get_contracted_point_on_the_inside(centroid, reflected, ro)
            fc = func.evaluate(contracted)
            if fc < fn1:
                self.replace_worst_point_in_simplex(simplex, contracted)
                continue

            self.replace_all_points_except_the_best(simplex, sigma)

        if not flag:
            ans.append(tuple([row[0] for row in self.get_centroid_of_a_simplex(simplex)]))
        self.number_of_steps = len(ans) - 1

        return ans

    @staticmethod
    def replace_worst_point_in_simplex(simplex, new_point):
        simplex.pop()
        simplex.append(new_point)

    @staticmethod
    def replace_all_points_except_the_best(simplex, sigma):
        x1 = simplex[0]
        for i, xi in enumerate(simplex):
            if i == 0:
                continue
            shrunk = x1.copy()
            shrunk += sigma * (xi - x1)
            simplex[i] = shrunk

    @staticmethod
    def get_contracted_point_on_the_inside(centroid, worst, ro):
        rs = centroid.copy()
        rs += ro * (worst - centroid)
        return rs

    @staticmethod
    def get_contracted_point_on_the_outside(centroid, reflected, ro):
        rs = centroid.copy()
        rs += ro * (reflected - centroid)
        return rs

    @staticmethod
    def get_expanded_point(centroid, reflected, gamma):
        rs = centroid.copy()
        rs += gamma * (reflected - centroid)
        return rs

    @staticmethod
    def get_reflected_point(centroid, worst, alpha):
        rs = centroid.copy()
        rs += alpha * (centroid - worst)
        return rs

    @staticmethod
    def get_canonical_vector(i, n):
        rs = np.zeros((n, 1), int)
        rs[i - 1] = 1
        return rs

    @staticmethod
    def get_initial_simplex(centroid, n):
        rs = []
        for i in range(n):
            i += 1
            ei = NelderMeadOptimizer.get_canonical_vector(i, n) * 0.5
            rs.append(ei + centroid.copy())

        last_simplex_vertex = centroid.copy()
        last_simplex_vertex *= (n + 1)
        for v in rs:
            last_simplex_vertex -= v

        rs.append(last_simplex_vertex)

        return rs

    @staticmethod
    def get_centroid_of_a_simplex(simplex):
        c = simplex[0].copy()
        for v in simplex:
            c += v
        c -= simplex[0]
        c /= len(simplex)
        return c
