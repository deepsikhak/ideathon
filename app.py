from flask import Flask, jsonify, request, json

app = Flask(__name__)


@app.route('/home', methods=['GET'])
def getDetails():
    response = app.response_class(response=json.dumps({"data":"Hello world"}), status=200, mimetype='application/json')
    return response



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)