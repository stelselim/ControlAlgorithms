import control as control
import json as json
import numpy as np

# Parameters
# sys: StateSpace, or TransferFunction
# Returns x and y points
# Ex: {'x':[1,2,3],'y':[1,4,9]}


def polesAndZeros(sys: control.TransferFunction):
    poles = control.pole(sys).tolist()
    zeros = control.zero(sys).tolist()
    pList = []
    zList = []

    for e in poles:
        val: complex = e
        real = round(val.real,5)
        imag = round(val.imag,5)
        pList.append({"real":real,"imag":imag})
        
    for e in zeros:
        val: complex = e
        real = round(val.real,5)
        imag = round(val.imag,5)
        zList.append({"real":real,"imag":imag})
        
    return json.dumps({"zeros":zList,"poles":pList})

# For Debugging
# a = polesAndZeros(control.TransferFunction([1, 4, 5, 6], [1, 5, 6, 7, 2]))
# print(a)
