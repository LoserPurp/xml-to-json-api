# About
The purpose of this application is to convert XML data fetched from specific endpoints into JSON format. It provides an API where you can specify an endpoint path, and the application will retrieve XML data from the configured endpoint, convert it to JSON, and return the JSON response.  

# How to use

## Installation
* Install python
* Clone the repo with
```console
git clone https://github.com/LoserPurp/xml-to-json-api.git
```
* Go to the xml-to-json-api folder and install the python modules with
```console
pip install -r requirements.txt
```

## Make an endpoint
1. Open the conf.json.  
2. Add one or more lines to the file where you specify the endpoint `"/endpoint-name"` and the url `"https://url-to-api/data"`

Here is an example of what your endpoints will look like.
```json
{
    "/success": "https://mocktarget.apigee.net/xml",
    "/error": "https://mocktarget.apigee.net/xml2"
}
```
Note that you can name the endpoint whatever you want

## Use an endpoint
1. Open up the folder the script and json files are located and run `pyhton app.py`
3. Open up a browser and go to `http:your-ip:7236/your-endpoint` and you should see the data in a json format


## Notes
* The script does not support https.
* The script need to be started manually. You could make a systemd that runs the script automatically, but that is something you have to do yourself  
* If you want to change the port you can edit the server function at the last line of the script.  
* If you want the data to only be accessible from the machine that is running the script you can remove the host parameter in the last line of the script.  

This is what the serve function looks like by default
```python
serve(app, host="0.0.0.0", port="7236")
```
