from app import app
from flask_socketio import SocketIO, emit
from app_bone import create_app
import app_bone

socketio = SocketIO(app)
socketio.run(app, debug=True)

if __name__ == "__main__":
    app.run(debug=True)
