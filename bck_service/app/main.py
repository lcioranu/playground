
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/obtainetemp', methods=['GET'])
def endpoint1():
    response = {
        'message': '25'
    }
    return jsonify(response)

@app.route('/api/obtainpressure', methods=['GET'])
def endpoint2():
    response = {
        'message': '10psi'
        
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4520)