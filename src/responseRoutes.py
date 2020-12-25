from flask import Blueprint, request
import json as json
# pylint: disable=import-error
from src.utility.makeSystem import makeSystem  
from src.response.step import stepInfoSystem,stepResponseOfSystem  
from src.response.ramp import rampResponseOfSystem
from src.response.impulse import impulseResponseOfSystem


response = Blueprint('response', __name__, template_folder='templates')

@response.route('/stepresponse')
def stepresponseRouter():
    try:
        num = request.args.get('num')
        den = request.args.get('den')
        return stepResponseOfSystem(makeSystem(num,den))
    except:
        return json.dumps({"Error": "Error with stepresponse"}) 


@response.route('/stepinfo')
def stepinfoRouter():
    try:
        num = request.args.get('num')
        den = request.args.get('den')
        return stepInfoSystem(makeSystem(num,den))
    except:
        return json.dumps({"Error": "Error with stepinfo"}) 
   



@response.route('/rampresponse')
def rampresponseRouter():
    try:
        num = request.args.get('num')
        den = request.args.get('den')
        return rampResponseOfSystem(makeSystem(num,den))
    except:
        return json.dumps({"Error": "Error with rampresponse"}) 

    

@response.route('/impulseresponse')
def impulseresponseRouter():
    try:
        num = request.args.get('num')
        den = request.args.get('den')
        return impulseResponseOfSystem(makeSystem(num,den))
    except:
        return json.dumps({"Error": "Error with impulseresponse"}) 
    
