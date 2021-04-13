from flask import Flask
import login

app = Flask(__name__)

@app.route("/login")
def start():
    login.start()