from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from time import time
import numpy as np
from math import e
import os


class Plotter:
    def __init__(self, record=None, def_x: tuple = (-2, 2), def_y: tuple = (-2, 2), density: int = 100,
                 save_to_folder: str = None, logspace_arguments: tuple = (-1, 3, 50)):
        self.record = record
        self.func = record.func.func if record is not None else None
        self.optimizer_path = record.optimizer_path if record is not None else None
        self.record_has_been_loaded = (record is not None)

        self.def_x = def_x
        self.def_y = def_y
        self.density = density
        self.save_to_folder = save_to_folder
        self.logspace_arguments = logspace_arguments

    def surface_plot(self) -> None:
        assert self.record_has_been_loaded

        if self.save_to_folder is not None:
            if not os.path.exists(self.save_to_folder):
                os.mkdir(self.save_to_folder)

        # Create a grid of points in the x-y plane
        x = np.linspace(*self.def_x, self.density)
        y = np.linspace(*self.def_y, self.density)
        X, Y = np.meshgrid(x, y)

        # Evaluate the function at each point in the grid
        Z = self.func(X, Y)

        # Create a surface plot of the function
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.7)

        # Set the axis labels and title
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('f(x,y)')
        ax.set_title('Surface plot of f(x,y)')

        if len(self.optimizer_path) > 0:
            ax.scatter(self.optimizer_path[0][0], self.optimizer_path[0][1],
                       self.func(self.optimizer_path[0][0], self.optimizer_path[0][1]),
                       color='red', s=10, alpha=1.0)
        # Plot the optimizer's path on top of the surface plot
        for i in range(len(self.optimizer_path) - 1):
            ax.plot([self.optimizer_path[i][0], self.optimizer_path[i + 1][0]],
                    [self.optimizer_path[i][1], self.optimizer_path[i + 1][1]],
                    [self.func(self.optimizer_path[i][0], self.optimizer_path[i][1]),
                     self.func(self.optimizer_path[i + 1][0], self.optimizer_path[i + 1][1])],
                    color='red', linewidth=2, alpha=1.0)
            # Add red balls to the points in the optimizer's path
            ax.scatter(self.optimizer_path[i + 1][0], self.optimizer_path[i + 1][1],
                       self.func(self.optimizer_path[i + 1][0], self.optimizer_path[i + 1][1]),
                       color='red', s=10, alpha=1.0)

        if self.save_to_folder is not None:
            plt.savefig(os.path.join(self.save_to_folder, f'{self.record.get_label()}_{time}.png'))

        # Show the plot
        if self.save_to_folder is None:
            plt.show()

    def contour_plot(self) -> None:
        assert self.record_has_been_loaded

        if self.save_to_folder is not None:
            if not os.path.exists(self.save_to_folder):
                os.mkdir(self.save_to_folder)

        # Create a grid of points in the x-y plane
        x = np.linspace(*self.def_x, self.density)

        y = np.linspace(*self.def_y, self.density)
        X, Y = np.meshgrid(x, y)

        # Evaluate the function at each point in the grid
        Z = self.func(X, Y)

        # Create a contour plot of the function
        fig, ax = plt.subplots()
        ax.contour(X, Y, Z, levels=np.logspace(*self.logspace_arguments))

        # Set the axis labels and title
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Contour plot of f(x,y)')

        if len(self.optimizer_path) > 0:
            ax.scatter(self.optimizer_path[0][0], self.optimizer_path[0][1], color='red', s=10)
        # Plot the optimizer's path on top of the contour plot
        for i in range(len(self.optimizer_path) - 1):
            ax.plot([self.optimizer_path[i][0], self.optimizer_path[i + 1][0]],
                    [self.optimizer_path[i][1], self.optimizer_path[i + 1][1]],
                    color='red')
            ax.scatter(self.optimizer_path[i + 1][0], self.optimizer_path[i + 1][1], color='red', s=10)

        if self.save_to_folder is not None:
            plt.savefig(os.path.join(self.save_to_folder, f'{self.record.get_label()}_{time()}.png'))

        # Show the plot
        if self.save_to_folder is None:
            plt.show()

    def set_record(self, value):
        self.record = value
        self.func = value.func.func
        self.optimizer_path = value.optimizer_path
        self.record_has_been_loaded = True
