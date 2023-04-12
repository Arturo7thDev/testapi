from flask import Flask, jsonify, request
from subscription import Subscription
import json

app = Flask(__name__)

from suscriptions import suscriptions

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

@app.route('/suscriptions', methods=['GET'])
def getData():
    return jsonify({"suscriptions": suscriptions})


@app.route('/register', methods=['POST'])
def create_subscription():
    data = json.loads(request.data)
    name = data['name']
    amount = data['amount']
    
    subscription = Subscription(name, amount)
    print(subscription)
    return {'success': True}

if __name__ == '__main__':
    app.run(debug=True, port=4000)
