from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

connected_users = set()

@socketio.on('connect')
def handle_connect():
    connected_users.add(request.sid)
    print(f"User connected: {request.sid}, total: {len(connected_users)}")

@socketio.on('disconnect')
def handle_disconnect():
    connected_users.discard(request.sid)
    print(f"User disconnected: {request.sid}, total: {len(connected_users)}")

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

#threadch1 = threading.Thread(target=handle_client_datach1)
#threadch1.daemon = True
#threadch1.start()
#threadch2 = threading.Thread(target=handle_client_datach2)
#threadch2.daemon = True
#threadch2.start()
#threadch3 = threading.Thread(target=handle_client_datach3)
#threadch3.daemon = True
#threadch3.start()

if __name__ == '__main__':
    socketio.run(app, debug=True)
