from src.response.step import stepResponseOfSystem,stepInfoSystem
from flask import Flask, request
import control as control
from src.routes.analysisRoutes import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)


@app.route('/')
def hello():
    sys = control.TransferFunction([1], [1, 4, 15])
    a = stepInfoSystem(sys)
    return a


if __name__ == '__main__':
    app.run(threaded=True, port=8080)
