import control as control
import json as json
import numpy as np

# Parameters
# sys: StateSpace, or TransferFunction
# Returns x and y points
# Ex: {'x':[1,2,3],'y':[1,4,9]}

def impulseResponseOfSystem(sys: control.TransferFunction):
    res = control.impulse_response(sys)
    x = res[0].tolist()
    y = res[1].tolist()
    response = {"x": x, "y": y}
    return json.dumps(response)

