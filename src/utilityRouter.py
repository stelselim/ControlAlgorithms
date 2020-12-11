from flask import Blueprint, request, json
# pylint: disable=import-error
from src.utility.makeSystem import makeSystem
from src.utility.makeClosedLoop import makeClosedLoopSystem
from src.utility.makeClosedLoopUnitFeedback import makeClosedLoopWithUnitSystem


utility = Blueprint('utility', __name__, template_folder='templates')


@utility.route('/makeclosedloop')
def makeclosedloopRouter():
    try:
        num = request.args.get('num')
        den = request.args.get('den')
        feedbackNum = request.args.get('feedbackNum')
        feedbackDen = request.args.get('feedbackDen')
        sys = makeClosedLoopSystem(num, den, feedbackNum, feedbackDen)
        sysNum = sys.num[0][0]
        sysDen = sys.den[0][0]
        return json.dumps({"systemNumerator": sysNum.__str__(),"systemDenominator":sysDen.__str__()})
    except:
        return json.dumps({"Error": "Error with makeclosedloop"})

@utility.route('/closedloop/unitfeedback')
def closedloopWithUnitFeedbackRouter():
    try:
        num = request.args.get('num')
        den = request.args.get('den')
        sys = makeClosedLoopWithUnitSystem(num, den)
        sysNum = sys.num[0][0]
        sysDen = sys.den[0][0]
        return json.dumps({"systemNumerator": sysNum.__str__(),"systemDenominator":sysDen.__str__()})
    except:
        return json.dumps({"Error": "Error with closedloop with unitfeedback"})

@utility.route('/makesystem')
def makeSystemRouter():
    try:
        num = request.args.get('num')
        den = request.args.get('den')
        sys = makeSystem(num, den)
        sysNum = sys.num[0][0]
        sysDen = sys.den[0][0]
        return json.dumps({"systemNumerator": sysNum.__str__(),"systemDenominator":sysDen.__str__()})
    except:
        return json.dumps({"Error": "Error with makesystem"})
