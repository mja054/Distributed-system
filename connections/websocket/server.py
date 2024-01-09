from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message_from_client')
def handle_message(message):
    print('Received message:', message)
    # Send a response back to the client
    socketio.emit('message_from_server', 'Server received: ' + message)

if __name__ == '__main__':
    socketio.run(app, debug=True)

