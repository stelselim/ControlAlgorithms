
import control as control

# A function used to make closed loop system with unit feedback for given parameters
# Parameters:
#   numerator: num [str]
#   denominator: den [str]
#   Ex:
#   --> num = 1,2,-3,5
#   --> den = 2,1,5,67,2
# Returns: control.TransferFunction

def makeClosedLoopWithUnitSystem(num: str, den: str) -> control.TransferFunction:
    num = num.split(',')
    den = den.split(',')

    numInt = []
    denInt = []
    for e in num:
        numInt.append(int(e))

    for e in den:
        denInt.append(int(e))

    sys = control.TransferFunction(numInt, denInt)
    return control.feedback(sys, 1)

