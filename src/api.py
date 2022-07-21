import json

import requests
import werkzeug
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)


@app.route('/upload', methods=['POST'])
def uploadAddressData():
    parser = reqparse.RequestParser()
    parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
    args = parser.parse_args()
    if 'file' not in args:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    datafile = args.get('file')
    response = processAddressFile(datafile)
    print(f"post message: {datafile}")
    return jsonify(response)


def processAddressFile(datafile):
    addrURL = "https://"
    addrSrcDf = pd.read_csv(datafile, delimiter=',', header=0, doublequote=True)
    addrSrcJson = json.loads(addrSrcDf.to_json(orient="records"))
    print(addrSrcJson)
    # addressVerifyResp = requests.post(addrURL, json = addSrcJson)
    addressVerifyResp = [{"addressid":"A","address1":"B","fulladdress":"A|B|C|D|E"}]
    print(addressVerifyResp)
    return addressVerifyResp


if __name__ == '__main__':
    app.run(debug=True, port=8080)  # , host="0.0.0.0")
