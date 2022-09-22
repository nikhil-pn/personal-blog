from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)
responses = requests.get(url="https://api.npoint.io/df94b1d7e55b35de9930")
data = responses.json()


@app.route('/')
def home():
    return render_template('index.html', data=data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<nu>')
def post(nu):
    n = int(nu) - 1
    return render_template('post.html', num=n, data=data)


sucess_true = "true"


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        name = request.form.get("text_name")
        email = request.form.get("text_email")
        phone = request.form.get("text_phone")
        message = request.form.get("text_message")
        print(name, "\n", email, phone, message)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="email address", password="yourpassword for smtplib")
            connection.sendmail(from_addr="a from eamil adress",
                                to_addrs="the email address that will revieve messages",
                                msg=f"Subject:{name} has send a message\n\nEmail:{email}\nPhone:{phone}  Message :{message} ")

        return render_template("contact.html", msg_sent=True)

    return render_template('contact.html', msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
