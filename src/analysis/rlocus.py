import control as control
import json as json
import numpy as np

# Parameters
# sys: StateSpace, or TransferFunction
# Returns x and y points
# Ex: {'x':[1,2,3],'y':[1,4,9]}


# Now SISO Only
def rlocusOfSystem(sys: control.TransferFunction):
    
    if not control.issiso(sys):
        return json.dumps({"Error":"Only Single Input Single Output"})

    res = control.root_locus(sys,Plot=False) # pylint: disable=no-member
    points = []
    x = res[0].tolist()
    y = res[1].tolist()
    for i in range(len(x)):
        points.append([x[i][0],y[i]])
    print(points)
    response = {"points":points}
    return json.dumps(response)
# For Debugging
# a = rlocusOfSystem(control.TransferFunction([1],[1,2]))
# print(a)