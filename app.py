from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    # Email Settings
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    # SAVE AS AN ENVIRONMENTAL VARIABLE SO NO ONE STEAL THIS INFO!!!
    MAIL_USERNAME="seanohioroberts@gmail.com",
    MAIL_PASSWORD="Qazwsxujm77"
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
        return redirect("/contact")
    else:
        return render_template("contact.html")


if __name__ == "__main__":
    app.run(port=8000)
