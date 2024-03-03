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

NUMBER_OF_STEPS = 10000

if __name__ == '__main__':
    opts = {}
    for eta in [10, 5, 2, 1, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001]:
        opts[f'GD-{eta}'] = GradientDescentOptimizer(f'GD, lr {eta}', NUMBER_OF_STEPS, eta)
        opts[f'GDM-{eta}'] = MomentumGradientDescentOptimizer(f'GDM, lr {eta}', NUMBER_OF_STEPS, eta)
        opts[f'NAG-{eta}'] = NesterovAcceleratedGradientOptimizer(f'NAG, lr {eta}', NUMBER_OF_STEPS, eta)
        opts[f'AdaGrad-{eta}'] = AdaptiveGradientOptimizer(f'AdaGrad, lr {eta}', NUMBER_OF_STEPS, eta)
        opts[f'Adam-{eta}'] = AdaptiveMomentEstimationOptimizer(f'Adam, lr {eta}', NUMBER_OF_STEPS, eta)

    # opts['NM'] = NelderMeadOptimizer("Nelder Mead", NUMBER_OF_STEPS, None)

    funcs = {
        # "quad": MathFunction("Quadratic function", lambda x, y: x ** 2 + 2 * y ** 2, lambda x, y: (2 * x, 4 * y), (0,0)),
        "pring": MathFunction("Hyperbolic paraboloid", lambda x, y: 1 / 10 * (x ** 2 - y ** 2),
                              lambda x, y: (1 / 5 * x, -1 / 5 * y), (0, 0)),
        # "rsb": MathFunction("Rosenbrock function", lambda x, y: (1 - x) ** 2 + 100 * (y - x ** 2) ** 2,
        #                     lambda x, y: (- 2 * (1 - x) + 200 * (y - x ** 2) * (- 2 * x), 200 * (y - x ** 2)), (1, 1)),
    }

    # funcs["pring"].set_commentary("Pozor, desired_minimum je nastaveno na stacionární bod - tam se stejně všechny metody seknou.")

    OR = OptimizationRecord

    records = [
        # OR(opts["GD-0.1"], funcs["quad"], (2.0, 1.5)),
        # OR(opts["GD-0.5"], funcs["pring"], (1.0, 0.0)),
        # OR(opts["GD-0.001"], funcs["rsb"], (2.0, 1.5)),
        # OR(opts["GD-0.005"], funcs["rsb"], (0.0, 0.0)),
        # OR(opts["GDM-0.5"], funcs["quad"], (2.0, 1.5)),
        # OR(opts["GDM-1.0"], funcs["pring"], (1.0, 0.0)),
        # OR(opts["GDM-0.001"], funcs["rsb"], (2.0, 1.5)),
        # OR(opts["GDM-0.015"], funcs["rsb"], (0.0, 0.0)),
        # OR(opts["NAG-2.0"], funcs["quad"], (2.0, 1.5)),
        # OR(opts["NAG-5.0"], funcs["pring"], (1.0, 0.0)),
        # OR(opts["NAG-0.001"], funcs["rsb"], (2.0, 1.5)),
        # OR(opts["NAG-0.005"], funcs["rsb"], (0.0, 0.0)),
        # OR(opts["AdaGrad-3.0"], funcs["quad"], (2.0, 1.5)),
        # OR(opts["AdaGrad-3.0"], funcs["pring"], (1.0, 0.0)),
        # OR(opts["AdaGrad-1.0"], funcs["rsb"], (2.0, 1.5)),
        # OR(opts["AdaGrad-0.2"], funcs["rsb"], (0.0, 0.0)),
        # OR(opts["Adam-2.0"], funcs["quad"], (2.0, 1.5)),
        # OR(opts["Adam-1.0"], funcs["pring"], (1.0, 0.0)),
        # OR(opts["Adam-0.007"], funcs["rsb"], (2.0, 1.5)),
        # OR(opts["Adam-0.1"], funcs["rsb"], (0.0, 0.0)),
        # OR(opts["NM"], funcs["quad"], (2.0, 1.5)),
        # OR(opts["NM"], funcs["rsb"], (2.0, 1.5)),
        # OR(opts["NM"], funcs["rsb"], (0.0, 0.0)),
    ]

    for _, opt in opts.items():
        for _, func in funcs.items():
            records.append(OR(opt, func, (1.0, 0.0)))

    records.sort(key=lambda k: k.label)

    core = Core(records)
