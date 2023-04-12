from flask import Flask, jsonify

app = Flask(__name__)

from suscriptions import suscriptions

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

@app.route('/suscriptions', methods=['GET'])
def getData():
    return jsonify(suscriptions)


if __name__ == '__main__':
    app.run(debug=True, port=4000)
