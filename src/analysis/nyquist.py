import control as control
import json as json
import numpy as np

# Parameters
# sys: StateSpace, or TransferFunction
# Returns x and y points
# Ex: {'x':[1,2,3],'y':[1,4,9]}

def nyquistPlotOfSystem(sys: control.TransferFunction):
    
    res = control.nyquist_plot(sys,Plot=False)
    real = res[0].tolist()
    imag = res[1].tolist()
    freq = res[2].tolist()
    response = {"real": real, "imag": imag,"freq":freq}
    return json.dumps(response)
        
# For Debugging
# nyquistPlotOfSystem(control.TransferFunction([1],[1,2]))