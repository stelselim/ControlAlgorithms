import control as control
import json as json
import io
import numpy as np
from flask import Response
import matplotlib.pyplot as plot
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Parameters
# sys: StateSpace, or TransferFunction
# Returns x and y points
# Ex: {'x':[1,2,3],'y':[1,4,9]}


# Now SISO Only
def rlocusOfSystem(sys: control.TransferFunction):

    if not control.issiso(sys):
        return json.dumps({"Error": "Only Single Input Single Output"})
        
    res,a,image = control.root_locus(sys, Plot=True,grid=False)  # pylint: disable:unused-variable
    fig = image
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
    
# For Debugging
# rlocusOfSystem(control.TransferFunction([1], [1, 5, 6, 12, 2]))
# print(a)
