from src.responseRoutes import response
from src.analysisRoutes import analysis
from src.utilityRouter import utility
from werkzeug.exceptions import InternalServerError
from werkzeug.exceptions import HTTPException
from flask import Flask, request, render_template
import markdown

app = Flask(__name__)

app.register_blueprint(response)
app.register_blueprint(analysis)
app.register_blueprint(utility)


# An Error Occured
@app.errorhandler(Exception)
def handle_exception(e):
    return """<div style='padding:15'>
    <h1>Page Not Found</h1> \nPlease, check <a href=\"https://controlalgo.ey.r.appspot.com/\"> the documentation.</a> <br>https://controlalgo.ey.r.appspot.com/
    </div>"""


@app.route('/')
def welcomePage():
    f = open('home.md', 'r') 
    md = f.read()
    f.close()
    return markdown.markdown(md)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
