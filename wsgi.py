from flask import Flask
import login

app = Flask(__name__)

@app.route("/login")
def start():
    return(login.login_loop())