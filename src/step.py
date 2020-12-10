import control as control

def stepResponseOfSystem(sys: control.TransferFunction):
    
    a = control.step_info(sys)
    return a

def stepInfoSystem(sys: control.TransferFunction) -> dict:
    a = control.step_info(sys)
    return a

