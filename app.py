from src.response.step import stepResponseOfSystem, stepInfoSystem
from src.responseRoutes import response
from flask import Flask, request
import control as control



app = Flask(__name__)
app.register_blueprint(response)

@app.route('/')
def welcomePage():
    return "<h1>Welcome To Control Algorithms</<h1>"


if __name__ == '__main__':
    app.run(threaded=True, port=8080)
