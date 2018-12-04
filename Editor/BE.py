import json
from pathlib import Path

import socketio
import eventlet
from flask import Flask, render_template, request
import Taboo


def backend():
    sio = socketio.Server()
    app = Flask(__name__)


    def readFile():
        filePath = Path('../cache')

        if filePath.is_file():
            f = open("../cache", "r")
            result = f.read()
            return result

    def writeFile(data):
        f = open("../cacheModified", "w")
        f.write(data)

    @app.route('/')
    def index():
        """Serve the client-side application."""
        return render_template('index.html')

    @app.route('/postmethod', methods=['POST'])
    def get_post_javascript_data():
        jsdata = request.form['javascript_data']
        writeFile(jsdata)
        return jsdata

    @app.route('/openfile')
    def get_file_data():
        data = readFile()
        return json.dumps(data)

    @app.route('/taboo')
    def get_taboo_data():
        taboo = Taboo.getTaboo()
        return json.dumps(taboo)

    @sio.on('connect')
    def connect(sid, environ):
        print('connect')

    @sio.on('input')
    def message(sid, data):
        sio.emit('input',data)

    @sio.on('disconnect')
    def disconnect(sid):
        print('disconnect ', sid)



    start = socketio.WSGIApp(sio, app)
    eventlet.wsgi.server(eventlet.listen(('localhost', 8000)), start)




if __name__ == '__main__':
    #BE = threading.Thread(target=backend, args=())
    #BE.daemon=True
    #BE.start()

    backend()

    #os.system("ssh -R LLHC:80:localhost:8000 serveo.net")