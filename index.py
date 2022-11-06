from flask import Flask, render_template, request

from config import Config
from simulation import time_space_simulation, fundamental_diagram_simulation

app = Flask(__name__,
            static_url_path='',
            static_folder=Config.png_dir,
            template_folder=Config.templates)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_inputs = request.form
        for key in form_inputs:
            value = form_inputs[key]
            if key == "road_size" and 2 < int(value) < 1000:
                Config.road_size = int(value)
            if key == "noise" and 0.0 <= float(value) <= 1.0:
                Config.noise = float(value)
            if key == "cars_amount" and 2 < int(value) < Config.road_size:
                Config.cars_amount = int(value)
            if key == "time_range" and 1 < int(value) < 500:
                Config.time_range = int(value)
        if request.form.get('time-space') == 'time-space':
            time_space_simulation()
        if request.form.get('fundamental') == 'fundamental':
            fundamental_diagram_simulation()
    return render_template('index.html',
                           road_size=Config.road_size,
                           noise=Config.noise,
                           cars_amount=Config.cars_amount,
                           time_range=Config.time_range)


if __name__ == '__main__':
    app.run(port=6666, host="0.0.0.0")
