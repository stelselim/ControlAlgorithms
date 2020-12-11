import control as control
import json as json
import numpy as np

# Parameters
# sys: StateSpace, or TransferFunction
# Returns x and y points
# Ex: {'x':[1,2,3],'y':[1,4,9]}

def bodePlotOfSystem(sys: control.TransferFunction):
    res = control.bode_plot(sys)
    mag = res[0].tolist()
    phase = res[1].tolist()
    omega = res[2].tolist()
    response = {"mag": mag, "phase": phase,"omega":omega}
    return json.dumps(response)

# For Debugging
# a = bodePlotOfSystem(control.TransferFunction([1],[1,2]))
# print(a)