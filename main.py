from flask import Flask, render_template, jsonify
from os import environ
from lora import mqttc_start
from threading import Thread

app = Flask(__name__)
GOOGLE_API_KEY = environ['GOOGLE_API_KEY']

@app.route('/')
def index():
    return render_template('index.html', key=GOOGLE_API_KEY)

@app.route('/distance')
def distance():
    return jsonify({
        'hscclab': environ['hscclab'],
        'lib': environ['lib'],
        'sci5': environ['sci5'] 
    })

if __name__ == '__main__':
    environ['sci5'] = '0'
    environ['hscclab'] = '0'
    environ['lib'] = '0'
    mqttc_thread = Thread(target=mqttc_start, daemon=True)
    mqttc_thread.start()
    app.run(port = int(environ.get("PORT", 5000)))
