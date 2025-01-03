from flask import Flask, render_template, url_for, request
from connect import messages, send_message

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def homepage():
    is_name = False
    name = ""
    
    if request.method == "POST":
        action = request.form.get("action")

        if action == "save":
            name = request.form.get("name")
            is_name = True

        if action == "edit":
            is_name = False

        if action == "send":
            message = request.form.get("message")

            send_message(name, message)

    return render_template("main.html", messages = messages.data, NOME = name, IS_NAME=is_name)


if __name__ == '__main__':
    app.run(debug = True) 

