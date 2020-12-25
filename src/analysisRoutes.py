from flask import Blueprint, request
import json as json
# pylint: disable=import-error
from src.utility.makeSystem import makeSystem  
from src.analysis.bode import bodePlotOfSystem
from src.analysis.nyquist import nyquistPlotOfSystem
from src.analysis.rlocus import rlocusOfSystem


analysis = Blueprint('analysis', __name__, template_folder='templates')

@analysis.route('/bodeplot')
def bodePlotRouter():
    try:
        num = request.args.get('num')
        den = request.args.get('den')
        return bodePlotOfSystem(makeSystem(num,den))
    except:
        return json.dumps({"Error": "Error with bodePlotOfSystem"})

@analysis.route('/nyquistplot')
def nyquistPlotRouter():
    try:
        num = request.args.get('num')
        den = request.args.get('den')
        return nyquistPlotOfSystem(makeSystem(num,den))
    except:
        return json.dumps({"Error": "Error with nyquistPlotOfSystem"}) 
    


@analysis.route('/rlocusplot')
def rlocusPlotRouter():
    try:
        num = request.args.get('num')
        den = request.args.get('den')
        return rlocusOfSystem(makeSystem(num,den))
    except:
        return json.dumps({"Error": "Error with rlocusplotSystem"}) 
    
    