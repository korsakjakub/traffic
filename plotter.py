"""
Jakub Korsak
"""
from matplotlib import pyplot as plt
import numpy as np

from config import Config


class Plotter:
    """
    A class representing the set of tools needed for generating plots of Traffic
    """

    def __init__(self, data):
        self.data = data

    def time_space(self, plot_data):
        """
        :param plot_data: The data needed for plotting time-space diagrams.
        It contains filename and time_range
        """
        filename = plot_data['filename']
        time_range = plot_data['time_range']
        positions = self.data

        plt.figure()
        plt.xlabel("time [a. u.]")
        plt.ylabel("space [a. u.]")
        plt.ylim([0, Config.road_size])
        plt.xlim([0, time_range])
        _ = [plt.plot(pos) for pos in positions]
        plt.savefig(filename, dpi=150)
        plt.close()

    def fix_pbc_artifacts(self):
        """
        It splits trajectories of cars which go around the road.
        """
        out_data_points = []
        for car_path in self.data:
            last_trim_index = 0
            for time in range(len(car_path) - 1):
                if car_path[time + 1] < car_path[time]:
                    comb = np.append(
                        np.zeros((last_trim_index,)),
                        car_path[last_trim_index:time + 1]
                    )
                    out_data_points.append(comb.tolist())
                    last_trim_index = time + 1
            comb = np.append(np.zeros((last_trim_index,)), car_path[last_trim_index:])
            out_data_points.append(comb.tolist())
        self.data = out_data_points
        return out_data_points

    def fundamental_diagram(self, plot_data):
        """
        Plot fundamental diagrams
        :param plot_data: The data needed for plotting fundamental diagrams.
        """
        filename = plot_data['filename']
        data = self.data

        plt.figure()
        plt.xlabel("density [cars/road size]")
        plt.ylabel("mean flux w.r.p. to position [cars/time]")
        plt.ylim([0, 1])
        plt.xlim([0, 1])
        plt.scatter(data[0], data[1])
        plt.savefig(filename, dpi=150)
        plt.close()
