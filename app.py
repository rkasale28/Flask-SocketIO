from flask import Flask, render_template
from flask_socketio import SocketIO
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET')

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return "Hello World"

@app.route('/template')
def template():
    return render_template("index.html")

@app.route('/sessions')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__=="__main__":
    app.run()