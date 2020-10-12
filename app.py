from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/contact", methods=["POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        msg = Message(
            message,
            subject="*Portfolio*" + name + "-" + subject,
            sender=email,
            recipients=["seanohioroberts@gmail.com"]
        )
        Mail.send(msg)
    else:
        return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
