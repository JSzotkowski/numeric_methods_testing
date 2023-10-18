import json

from includes.Core import Core
from includes.MathFunction import MathFunction
from includes.OptimizationRecord import OptimizationRecord
from includes.NelderMeadOptimizer import NelderMeadOptimizer
from includes.GradientDescentOptimizer import GradientDescentOptimizer
from includes.AdaptiveGradientOptimizer import AdaptiveGradientOptimizer
from includes.MomentumGradientDescentOptimizer import MomentumGradientDescentOptimizer
from includes.AdaptiveMomentEstimationOptimizer import AdaptiveMomentEstimationOptimizer
from includes.NesterovAcceleratedGradientOptimizer import NesterovAcceleratedGradientOptimizer

NUMBER_OF_STEPS = 500

if __name__ == '__main__':
    opts = {
        "GD-0.001": GradientDescentOptimizer("Gradient Descent, lr 0.001", NUMBER_OF_STEPS, 0.001),
        "GD-0.005": GradientDescentOptimizer("Gradient Descent, lr 0.005", NUMBER_OF_STEPS, 0.005),
        "GD-0.1": GradientDescentOptimizer("Gradient Descent, lr 0.1", NUMBER_OF_STEPS, 0.1),
        "GD-0.5": GradientDescentOptimizer("Gradient Descent, lr 0.5", NUMBER_OF_STEPS, 0.5),
        "GDM-0.001": MomentumGradientDescentOptimizer("Momentum Gradient Descent, lr 0.001", NUMBER_OF_STEPS, 0.001),
        "GDM-0.015": MomentumGradientDescentOptimizer("Momentum Gradient Descent, lr 0.015", NUMBER_OF_STEPS, 0.015),
        "GDM-0.5": MomentumGradientDescentOptimizer("Momentum Gradient Descent, lr 0.5", NUMBER_OF_STEPS, 0.5),
        "GDM-1.0": MomentumGradientDescentOptimizer("Momentum Gradient Descent, lr 0.1", NUMBER_OF_STEPS, 1),
        "NAG-2.0": NesterovAcceleratedGradientOptimizer("Nesterov Accelerated Gradient, lr 2.0", NUMBER_OF_STEPS, 2),
        "NAG-5.0": NesterovAcceleratedGradientOptimizer("Nesterov Accelerated Gradient, lr 5.0", NUMBER_OF_STEPS, 5),
        "NAG-0.001": NesterovAcceleratedGradientOptimizer("Nesterov Accelerated Gradient, lr 0.001", NUMBER_OF_STEPS,
                                                          0.001),
        "NAG-0.005": NesterovAcceleratedGradientOptimizer("Nesterov Accelerated Gradient, lr 0.005", NUMBER_OF_STEPS,
                                                          0.005),
        "AdaGrad-0.2": AdaptiveGradientOptimizer("Adaptive Gradient, lr 0.2", NUMBER_OF_STEPS, 0.2),
        "AdaGrad-1.0": AdaptiveGradientOptimizer("Adaptive Gradient, lr 1.0", NUMBER_OF_STEPS, 1.0),
        "AdaGrad-3.0": AdaptiveGradientOptimizer("Adaptive Gradient, lr 3.0", NUMBER_OF_STEPS, 3.0),
        "Adam-0.007": AdaptiveMomentEstimationOptimizer("Adaptive Moment Estimation, lr 0.007", NUMBER_OF_STEPS, 0.007),
        "Adam-0.1": AdaptiveMomentEstimationOptimizer("Adaptive Moment Estimation, lr 0.1", NUMBER_OF_STEPS, 0.1),
        "Adam-1.0": AdaptiveMomentEstimationOptimizer("Adaptive Moment Estimation, lr 1.0", NUMBER_OF_STEPS, 1.0),
        "Adam-2.0": AdaptiveMomentEstimationOptimizer("Adaptive Moment Estimation, lr 2.0", NUMBER_OF_STEPS, 2.0),
        "NM": NelderMeadOptimizer("Nelder Mead", NUMBER_OF_STEPS, 1.0),
    }

    funcs = {
        "quad": MathFunction("Quadratic function", lambda x, y: x ** 2 + 2 * y ** 2, lambda x, y: (2 * x, 4 * y), (0,0)),
        "pring": MathFunction("Hyeprbolic paraboloid", lambda x, y: 1 / 10 * (x ** 2 - y ** 2),
                              lambda x, y: (1 / 5 * x, -1 / 5 * y), (0, 0)),
        "rsb": MathFunction("Rosenbrock function", lambda x, y: (1 - x) ** 2 + 100 * (y - x ** 2) ** 2,
                            lambda x, y: (- 2 * (1 - x) + 200 * (y - x ** 2) * (- 2 * x), 200 * (y - x ** 2)), (1, 1)),
    }

    funcs["pring"].set_commentary("Pozor, desired_minimum je nastaveno na lokální minimum - tam se stejně všechny metody seknou.")

    OR = OptimizationRecord

    records = [
        OR(opts["GD-0.1"], funcs["quad"], (2.0, 1.5)),
        OR(opts["GD-0.5"], funcs["pring"], (1.0, 0)),
        OR(opts["GD-0.001"], funcs["rsb"], (2.0, 1.5)),
        OR(opts["GD-0.005"], funcs["rsb"], (0.0, 0.0)),
        OR(opts["GDM-0.5"], funcs["quad"], (2.0, 1.5)),
        OR(opts["GDM-1.0"], funcs["pring"], (1.0, 0)),
        OR(opts["GDM-0.001"], funcs["rsb"], (2.0, 1.5)),
        OR(opts["GDM-0.015"], funcs["rsb"], (0.0, 0.0)),
        OR(opts["NAG-2.0"], funcs["quad"], (2.0, 1.5)),
        OR(opts["NAG-5.0"], funcs["pring"], (1.0, 0)),
        OR(opts["NAG-0.001"], funcs["rsb"], (2.0, 1.5)),
        OR(opts["NAG-0.005"], funcs["rsb"], (0.0, 0.0)),
        OR(opts["AdaGrad-3.0"], funcs["quad"], (2.0, 1.5)),
        OR(opts["AdaGrad-3.0"], funcs["pring"], (1.0, 0)),
        OR(opts["AdaGrad-1.0"], funcs["rsb"], (2.0, 1.5)),
        OR(opts["AdaGrad-0.2"], funcs["rsb"], (0.0, 0.0)),
        OR(opts["Adam-2.0"], funcs["quad"], (2.0, 1.5)),
        OR(opts["Adam-1.0"], funcs["pring"], (1.0, 0)),
        OR(opts["Adam-0.007"], funcs["rsb"], (2.0, 1.5)),
        OR(opts["Adam-0.1"], funcs["rsb"], (0.0, 0.0)),
        OR(opts["NM"], funcs["quad"], (2.0, 1.5)),
        OR(opts["NM"], funcs["rsb"], (2.0, 1.5)),
        OR(opts["NM"], funcs["rsb"], (0.0, 0.0)),
    ]

    core = Core(records)


