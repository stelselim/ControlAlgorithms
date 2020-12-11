import control as control

# A function used to make closed loop system with custom feedback for given parameters
# Parameters:
#   numerator: num [str]
#   denominator: den [str]
#   feedback: feedback [str]
#   Ex:
#   --> num = 1,2,-3,5
#   --> den = 2,1,5,67,2
#   --> feedback = 1,2 or 1
# Returns: control.TransferFunction


def makeClosedLoopSystem(num: str, den: str, feedbackNum: str, feedbackDen: str) -> control.TransferFunction:
    num = num.split(',')
    den = den.split(',')
    feedbackNum = feedbackNum.split(',')
    feedbackDen = feedbackDen.split(',')
    numInt = []
    denInt = []
    feedbackNumInt = []
    feedbackDenInt = []
    for e in num:
        numInt.append(int(e))

    for e in den:
        denInt.append(int(e))

    for e in feedbackNum:
        feedbackNumInt.append(int(e))

    for e in feedbackDen:
        feedbackDenInt.append(int(e))

    sys = control.TransferFunction(numInt, denInt)
    sys2 = control.TransferFunction(feedbackNumInt, feedbackDenInt)
    return control.feedback(sys, sys2)


