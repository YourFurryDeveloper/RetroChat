from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message_chmain')
def handle_client_datach1(data):
    print(f"Data received from client (Channel: main): {data}")
    socketio.emit('response_chmain', {'message': f"{data['content']}"})

@socketio.on('message_chcasual')
def handle_client_datach2(data):
    print(f"Data received from client (Channel: casual): {data}")
    socketio.emit('response_chcasual', {'message': f"{data['content']}"})

@socketio.on('message_chschoolstuff')
def handle_client_datach3(data):
    print(f"Data received from client (Channel: schoolstuff): {data}")
    socketio.emit('response_chschoolstuff', {'message': f"{data['content']}"})

if __name__ == '__main__':
    socketio.run(app, debug=True)
