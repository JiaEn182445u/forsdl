from flask import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("llll.html")

#h
if __name__ == '__main__':
    app.run(port="80")
