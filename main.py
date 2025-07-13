from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


def auth(username, password):
    with open("data/data.json", encoding="utf-8") as f:
        users = json.load(f)
        for u in users:
            if u["username"] == username and u["password"] == password:
                return True

    return False;


if __name__ == "__main__":
    print(auth(username='admin', password="123"))
    app.run(debug=True)
