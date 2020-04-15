from flask import Flask
from flask.ext.aiohttp import AioHTTP

gameserver = Flask(__name__)

def create_gameserver():
    app = Flask(__name__)
    aio.init_app(app)

aio = AioHTTP()

# debug with werkzeug using aio.run(app, debug=True)
if __name__ == '__main__':
    aio.run(app)
