from plotter import Plotter
from traffic import Traffic
import numpy as np
from config import Config


# from plotter import Plotter


def calculate_flux(position, cars_positions):
    ticks = 0
    for car in cars_positions:
        smaller_than_pos = car[0] < position
        for t in range(len(car) - 1):
            if car[t] >= position and smaller_than_pos:
                smaller_than_pos = False
                ticks += 1
            if car[t + 1] < car[t]:
                smaller_than_pos = True
    return ticks / len(cars_positions[0])


def time_space_simulation():
    traffic = Traffic()
    traffic.get_initial_traffic(Config.cars_amount)
    time_range = Config.time_range
    positions = []
    for _ in range(time_range):
        traffic.move_cars()
        positions.append(traffic.get_cars_positions())
    plotter = Plotter(np.array(positions).T)
    plotter.fix_pbc_artifacts()
    plotter.time_space(plot_data={
        'filename': 'Traffic jam time-space diagram',
        'time_range': time_range
    })


def fundamental_diagram_simulation():
    plot_data = []
    for cars_amount in range(3, Config.road_size):
        traffic = Traffic()
        traffic.get_initial_traffic(cars_amount)
        time_range = Config.time_range
        positions = []
        for _ in range(time_range):
            traffic.move_cars()
            positions.append(traffic.get_cars_positions())
        flux = np.mean(
            [calculate_flux(position=x, cars_positions=np.array(positions).T) for x in range(Config.road_size)])
        density = cars_amount / Config.road_size
        plot_data.append([density, flux])
    plotter = Plotter(np.array(plot_data).T)
    plotter.fundamental_diagram(plot_data={
        'filename': f'{Config.png_dir}Fundamental_diagram_{Config.noise}.png',
    })


if __name__ == "__main__":
    # time_space_simulation()
    fundamental_diagram_simulation()
