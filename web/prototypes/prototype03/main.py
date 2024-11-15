from flask import Flask, render_template, url_for
from connect import messages

app = Flask(__name__)

@app.route("/")
def homepage():

    return render_template("main.html", messages=messages.data)

if __name__ == '__main__':
    app.run(debug = True) 

