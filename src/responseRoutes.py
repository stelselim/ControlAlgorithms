from flask import Blueprint, request
# pylint: disable=C0321
from src.utility.makeSystem import makeSystem  
from src.response.step import stepInfoSystem,stepResponseOfSystem  


response = Blueprint('response', __name__, template_folder='templates')

@response.route('/stepresponse')
def stepresponseRouter():
    num = request.args.get('num')
    den = request.args.get('den')
    return stepResponseOfSystem(makeSystem(num,den))


@response.route('/stepinfo')
def stepinfoRouter():
    num = request.args.get('num')
    den = request.args.get('den')
    return stepInfoSystem(makeSystem(num,den))












# @analysis.route('/step/', methods=['GET'])
# def hello(username):
#     return "Hello {}".format(username)


# @app.route('/tf')
# def home():
#     try:
#         x = stepResponseOfSystem(numInt,denInt)
#     except:
#         print("Problem")
#     return '<h1> Welcome To Server </h1> {}'.format(x)

# @app.route('/login/<username>', methods=['GET'])
# def hello(username):
#     return "Hello {}".format(username)
