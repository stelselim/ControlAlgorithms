from flask import Blueprint, request
# pylint: disable=import-error
from src.utility.makeSystem import makeSystem  
from src.analysis.bode import bodePlotOfSystem
from src.analysis.nyquist import nyquistPlotOfSystem
from src.analysis.rlocus import rlocusOfSystem


analysis = Blueprint('analysis', __name__, template_folder='templates')

@analysis.route('/bodeplot')
def bodePlotRouter():
    num = request.args.get('num')
    den = request.args.get('den')
    return bodePlotOfSystem(makeSystem(num,den))


@analysis.route('/nyquistplot')
def nyquistPlotRouter():
    num = request.args.get('num')
    den = request.args.get('den')
    return nyquistPlotOfSystem(makeSystem(num,den))



@analysis.route('/rlocusplot')
def rlocusPlotRouter():
    num = request.args.get('num')
    den = request.args.get('den')
    return rlocusOfSystem(makeSystem(num,den))
