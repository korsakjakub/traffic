from matplotlib import pyplot as plt
import numpy as np

from config import Config


class Plotter:
    def __init__(self, data):
        self.data = data

    def time_space(self, plot_data):
        filename = plot_data['filename']
        time_range = plot_data['time_range']
        positions = self.data

        plt.figure()
        plt.xlabel("time [a. u.]")
        plt.ylabel("space [a. u.]")
        plt.ylim([0, Config.road_size])
        plt.xlim([0, time_range])
        [plt.plot(pos) for pos in positions]
        plt.savefig(filename, dpi=150)
        plt.close()

    def fix_pbc_artifacts(self):
        out_data_points = []
        for car_path in self.data:
            last_trim_index = 0
            for t in range(len(car_path) - 1):
                if car_path[t + 1] < car_path[t]:
                    comb = np.append(np.zeros((last_trim_index,)), car_path[last_trim_index:t + 1])
                    out_data_points.append(comb.tolist())
                    last_trim_index = t + 1
            comb = np.append(np.zeros((last_trim_index,)), car_path[last_trim_index:])
            out_data_points.append(comb.tolist())
        self.data = out_data_points

    def fundamental_diagram(self, plot_data):
        filename = plot_data['filename']
        data = self.data

        plt.figure()
        plt.xlabel("density [cars/road size]")
        plt.ylabel("mean flux w.r.p. to position [cars/time]")
        plt.ylim([0, 1])
        plt.xlim([0, 1])
        plt.scatter(data[0], data[1])
        # [plt.plot(pos) for pos in positions]
        plt.savefig(filename, dpi=150)
        plt.close()
