import control as control
import json as json
import numpy as np

# Parameters 
# sys: StateSpace, or TransferFunction
# Returns x and y points
# Ex: {'x':[1,2,3],'y':[1,4,9]}
def stepResponseOfSystem(sys: control.TransferFunction):
    res = control.step_response(sys)
    x = res[0].tolist()
    y = res[1].tolist()
    response = {"x": x, "y": y}
    return json.dumps(response)


'''
From Original Documentation 
---------------------------


Parameters
sys: StateSpace, or TransferFunction

    LTI system to simulate  
T: array-like object, optional

    Time vector (argument is autocomputed if not given)  
SettlingTimeThreshold: float value, optional

    Defines the error to compute settling time (default = 0.02)  
RiseTimeLimits: tuple (lower_threshold, upper_theshold)

    Defines the lower and upper threshold for RiseTime computation 
     
Returns
S: a dictionary containing:

    RiseTime: Time from 10% to 90% of the steady-state value.  
    SettlingTime: Time to enter inside a default error of 2%  
    SettlingMin: Minimum value after RiseTime  
    SettlingMax: Maximum value after RiseTime  
    Overshoot: Percentage of the Peak relative to steady value  
    Undershoot: Percentage of undershoot  
    Peak: Absolute peak value  
    PeakTime: time of the Peak  
    SteadyStateValue: Steady-state value 

'''


def stepInfoSystem(sys: control.TransferFunction) -> str:
    a = control.step_info(sys)
    return json.dumps(a)
