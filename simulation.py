from traffic import Traffic
import time_space_plotter as tsp
import numpy as np
from config import Config


def simulation():
    traffic = Traffic()
    traffic.get_initial_traffic(Config.cars_amount)
    time_range = Config.time_range
    positions = []
    for _ in range(time_range):
        traffic.move_cars()
        positions.append(traffic.get_cars_positions())
    plot_positions = np.array(positions).T
    plot_positions = tsp.fix_pbc_artifacts(plot_positions)
    tsp.plot(plot_data={
        'filename': 'Traffic jam time-space diagram',
        'time_range': time_range,
        'positions': plot_positions,
    })
    #print(positions)


if __name__ == "__main__":
    simulation()
