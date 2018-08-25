from flask import Flask, jsonify, request, json
from flask_pymongo import PyMongo
import re


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/ideathon"
mongo = PyMongo(app)


@app.route('/home', methods=['GET'])
def getDetails():
    response = app.response_class(response=json.dumps({"data":"Hello world"}), status=200, mimetype='application/json')
    return response

@app.route('/mongo-test', methods=['GET'])
def MongoTest():
    vendors = mongo.db.vendors.find({})
    response = app.response_class(response=json.dumps({"data": vendors[0]["name"]}), status=200, mimetype='application/json')
    return response


@app.route('/get-vendors', methods=['GET'])
def GetVendors():
    pinCode = request.args.get("pin_code")
    deliveryArea = request.args.get("delivery_area")
    result = []
    if(pinCode):
        dbData = mongo.db.vendors.find({"pinCode": pinCode})
        for doc in dbData:
            result.append({
                "Name": doc["Name"],
                "Address": doc["address"],
                "Phone": doc["mobileNumber"],
                "HomeDelivery": doc["homeDelivery"]
            })
    elif(deliveryArea):
        regx = re.compile(deliveryArea, re.IGNORECASE)
        dbData = mongo.db.vendors.find({"delvieryArea": regx })
        for doc in dbData:
            result.append({
                "Name": doc["Name"],
                "Address": doc["address"],
                "Phone": doc["mobileNumber"],
                "HomeDelivery": doc["homeDelivery"]
            })

    response = app.response_class(response=json.dumps({"data":result}), status=200, mimetype='application/json')
    return response



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)