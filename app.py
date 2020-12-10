from src.step import stepResponseOfSystem
from flask import Flask, request

app = Flask(__name__)

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
   
    
if __name__ == '__main__':
    app.run(threaded=True, port=8000)
 
