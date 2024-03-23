from flask import Flask, jsonify, request
import requests
import xmltodict
import json

app = Flask(__name__)

#opens config file
with open('conf.json', 'r') as file:
    config = json.load(file)


#find the url in the conf file from the given endpoint
def find_endpoint(endpoint_path):
    for key, value in config.items():
        if key == endpoint_path:
            return value
    return None

#converts xml to json from config file and returns it
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def convert_xml_to_json(path):
    #fetch XML data from the endpoint

    #Construct the endpoint path
    endpoint_path = '/' + path
    url = find_endpoint(endpoint_path)
    if url:
        response = requests.get(url)
        #check if the request was successful
        if response.status_code == 200:
            #convert XML to JSON
            xml_data = response.text
            json_data = xmltodict.parse(xml_data)
            #return JSON data
            return jsonify(json_data)
        else:
            #return an error message if the request was not successful
            return jsonify({"error": "Failed to fetch XML data"}), 500
    else:
        #return an error message if the endpoint path is not found in the config
        return jsonify({"error": "Endpoint not configured"}), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="7236")
