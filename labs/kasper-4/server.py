from flask import Flask, Response, request, render_template
from blinkt import set_clear_on_exit, set_pixel, show
import time
import json

app = Flask(__name__)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colors = [red, green, blue]


def get_temp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    data = file.read().rstrip()  # remove trailing '\n' newline character.
    file.close()
    return round(int(data) / 1000, 2)


@app.route('/', methods=['GET'])
def home():
    payload = json.dumps({"temperature": get_temp()})
    return Response(payload, mimetype='application/json')

if __name__ == '__main__':

    app.run(debug=False, host='0.0.0.0')
