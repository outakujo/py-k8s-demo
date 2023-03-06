from flask import Flask, Response
import json
import socket
import requests

app = Flask(__name__)

@app.route('/')
def index():
    hn=socket.gethostname()
    return Response(json.dumps(hn, ensure_ascii=False), mimetype='application/json')

@app.route('/call')
def call():
    resp=requests.get(url="http://ads.ads:8080/abc")
    return Response(json.dumps(resp.text, ensure_ascii=False), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
