from flask import Flask, Response, request, render_template
from blinkt import set_clear_on_exit, set_pixel, show
import time
import json

app = Flask(__name__)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 190, 0)
pink = (255, 0, 255)
cyan = (0, 255, 255)


def get_temp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    data = file.read().rstrip()  # remove trailing '\n' newline character.
    file.close()
    return round(int(data) / 1000, 2)


def set_pixel_color(i, color):
    set_pixel(i, color[0], color[1], color[2])


@app.route('/', methods=['GET'])
def home():
    temperature = get_temp()
    for i in range(0, 8):
        aboveThirty = temperature - 32
        if aboveThirty == i:
            # mark
            set_pixel_color(i, yellow)
        elif aboveThirty > i:
            # warm
            set_pixel_color(i, red)
        else:
            # cold
            set_pixel_color(i, blue)
    show()
    payload = json.dumps({"temperature": temperature})
    return Response(payload, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
