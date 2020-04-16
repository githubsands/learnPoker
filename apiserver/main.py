import os
import yaml
from flask import Flask, redirect, url_for

class APIServer(Flask):
    def __init__(self, name):
        with open("config.yml", "r") as ymlfile:
            self.config = yaml.safe_load(ymlfile)
            self.redirect = self.config["lobbyserver_url"]

    def get_redirect():
        return self.redirect

app = APIServer(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def index():
    return redirect('/lobby')

@app.route('/lobby')
def redirect_to_lobby():
    return redirect(url_for(app.get_redirect()), 302, Response=none)
