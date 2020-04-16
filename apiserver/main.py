import os
import yaml
from flask import Flask, redirect, url_for

class APIServer(Flask):
    def __init__(self, name):
        with open("config.yml", "r") as ymlfile:
            self.config = yaml.safe_load(ymlfile)

app = APIServer(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def index():
    return redirect('/lobby')

@app.route('/lobby')
def redirect_to_lobby():
    return redirect(self.config["lobbyserver_url"], 302, Response=none)
