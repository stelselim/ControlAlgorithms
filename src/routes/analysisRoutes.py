from flask import Blueprint


simple_page = Blueprint('simple_page', __name__, template_folder='templates')
@simple_page.route('/login/<username>', methods=['GET'])
def hello(username):
    return "Hello {}".format(username)


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