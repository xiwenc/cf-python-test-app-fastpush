from flask import Flask
import os

app = Flask(__name__)

port = int(os.getenv("PORT", 9099))

@app.route('/')
def hello_world():
    return 'Hello World! I am instance ' + str(os.getenv("CF_INSTANCE_INDEX", 0))

@app.route('/sample.css')
def static_proxy():
    return app.send_static_file('sample.css')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
