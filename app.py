from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "KoboToolbox API Proxy is running."

@app.route('/get-data', methods=['POST'])
def get_data():
    data = request.json
    token = data.get('token')
    form_id = data.get('form_id')

    if not token or not form_id:
        return jsonify({'error': 'Missing token or form_id'}), 400

    url = f"https://kf.kobotoolbox.org/api/v2/assets/{form_id}/data/"
    headers = {"Authorization": f"Token {token}"}
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        return jsonify(res.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500