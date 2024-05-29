from flask import Flask, render_template
import socket

app = Flask(__name__)

def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip

@app.route('/')
def index():
    hostname, ip =get_ip()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=5010)