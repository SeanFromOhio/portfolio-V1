from flask import Flask, flash, render_template, request, redirect
from flask_mail import Mail, Message
import gunicorn
import os

app = Flask(__name__)
app.secret_key = os.environ.get("flask_key")
app.config.update(
    # Email Settings
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    # SAVE AS AN ENVIRONMENTAL VARIABLE SO NO ONE STEAL THIS INFO!!!
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
)
mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        subject_str = ("*Portfolio* " + name + " - " + subject)
        body_str = ("You've received a new contact from: " + email + "\n\n Message: \n\n" + message)

        msg = Message(
            body=body_str,
            subject=subject_str,
            sender=email,
            recipients=["seanohioroberts@gmail.com"],
        )
        mail.send(msg)
        flash("Message was sent! Thanks for reaching out to me.")
        return redirect("/contact")
    else:
        return render_template("contact.html")


if __name__ == "__main__":
    app.run(port=8000)
