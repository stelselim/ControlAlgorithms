import control as control
import json as json
import numpy as np

# Parameters
# sys: StateSpace, or TransferFunction
# Returns x and y points
# Ex: {'x':[1,2,3],'y':[1,4,9]}


# Now SISO Only
def rlocusOfSystem(sys: control.TransferFunction):
    try:
        if not control.issiso(sys):
            return json.dumps({"Error":"Only Single Input Single Output"})

        res = control.root_locus(sys,Plot=False) # pylint: disable=no-member
        x = res[0].tolist()
        y = res[1].tolist()
        response = {"x": x,"y":y}
        return json.dumps(response)
    except:
        return json.dumps({"Error": "Error with rlocusOfSystem"}) 
# For Debugging
# a = rlocusOfSystem(control.TransferFunction([1],[1,2]))
# print(a)