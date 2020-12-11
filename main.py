from src.responseRoutes import response
from src.analysisRoutes import analysis
from src.utilityRouter import utility
from flask import Flask, request
import markdown

app = Flask(__name__)
app.register_blueprint(response)
app.register_blueprint(analysis)
app.register_blueprint(utility)


@app.route('/')
def welcomePage():
    f = open('README.md', 'r') 
    md = f.read()
    f.close()
    return markdown.markdown(md)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
