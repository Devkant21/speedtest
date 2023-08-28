from flask import Flask, render_template, jsonify
from flask_cors import CORS
from speedtest import Speedtest

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speedtest')
def run_speed_test():

    st = Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping  # Ping in milliseconds

    return jsonify({
        'download_speed': download_speed,
        'upload_speed': upload_speed,
        'ping': ping
    })

if __name__ == '__main__':
    app.run(debug=True)
