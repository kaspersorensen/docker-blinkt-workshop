from flask import Flask, Response, request, render_template
from blinkt import set_clear_on_exit, set_pixel, show
import time
import json

app = Flask(__name__)


def get_temp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    data = file.read().rstrip()  # remove trailing '\n' newline character.
    file.close()
    return round(int(data) / 1000, 2)


@app.route('/', methods=['GET'])
def home():
    temperature = get_temp()
    for i in range(0, 8):
        aboveThirty = temperature - 30
        if aboveThirty == i:
            set_pixel(i, 255, 0, 0)
        elif aboveThirty > i:
            set_pixel(i, 0, 0, 255)
        else:
            set_pixel(i, 0, 255, 0)
    show()
    payload = json.dumps({"temperature": temperature})
    return Response(payload, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
