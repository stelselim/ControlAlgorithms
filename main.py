from src.response.step import stepResponseOfSystem, stepInfoSystem
from src.responseRoutes import response
from flask import Flask, request
import control as control
from src.response.ramp import rampResponseOfSystem



app = Flask(__name__)
app.register_blueprint(response)

@app.route('/')
def welcomePage():
    return "<h1>Welcome To Control Algorithms</<h1>"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

