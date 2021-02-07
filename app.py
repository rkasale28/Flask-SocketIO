from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

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
    socketio.run(app, cors_allowed_origins=['http://url', 'https://url'], host='0.0.0.0', port=5000)