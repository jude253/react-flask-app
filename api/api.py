import time
from flask import Flask

app = Flask(__name__)

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')
