from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
sio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def test():
    return 'hello world !'


@sio.on('connect')
def connect():
    print('\n\n connected \n\n')


@sio.on('disconnect')
def diconnect():
    print('\n\n disconnected \n\n')


@sio.on('ask-for-counter-update')
def handle_message():
    global counter
    counter += 1
    print(f"counter {counter}")
    emit("update-counter", {"counter": counter}, broadcast=True)


if __name__ == '__main__':
    counter = 0
    sio.run(app, debug=True)
