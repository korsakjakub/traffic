from matplotlib import pyplot as plt
import numpy as np

from config import Config


def plot(plot_data):
    filename = plot_data['filename']
    time_range = plot_data['time_range']
    positions = plot_data['positions']

    plt.figure()
    plt.xlabel("time [a. u.]")
    plt.ylabel("space [a. u.]")
    plt.ylim([0, Config.road_size])
    plt.xlim([0, time_range])
    [plt.plot(pos) for pos in positions]
    plt.savefig(filename, dpi=150)
    plt.close()


def fix_pbc_artifacts(data_points):
    out_data_points = []
    for car_path in data_points:
        last_trim_index = 0
        for t in range(len(car_path) - 1):
            if car_path[t + 1] < car_path[t]:
                comb = np.append(np.zeros((last_trim_index,)), car_path[last_trim_index:t+1])
                out_data_points.append(comb.tolist())
                last_trim_index = t + 1
        comb = np.append(np.zeros((last_trim_index,)), car_path[last_trim_index:])
        out_data_points.append(comb.tolist())
    return out_data_points
