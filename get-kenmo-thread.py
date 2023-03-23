import requests
import json
import os
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def post_response():
    request_dict = request.get_json()
    req_data = str(request_dict['data'])
    print(req_data)

    response = requests.get('https://itest.5ch.net/subbacks/poverty.json')
    print(response.status_code)
    print(response.json())
    res = response.json()
    json_str = json.dumps(res)

    result = {}
    result['origin'] = req_data
    result['data'] = json_str
    return result

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
