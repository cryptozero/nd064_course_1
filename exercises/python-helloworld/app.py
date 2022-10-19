from flask import Flask
import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# Logging a CUSTOM message 
app.logger.info('Main request successfull')


@app.route('/status')
def status():
  response = app.response_class(
          response=json.dumps({"result":"OK - healthy"}),
          status=200,
          mimetype='application/json'
  )
  app.logger.info('Status request successfull')
  return response

@app.route('/metrics')
def metrics():
  response = app.response_class(
          response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
          status=200,
          mimetype='application/json'
  )
  app.logger.info('Metrics request successfull')
  return response

if __name__ == "__main__":
    # Stream logs to a file, and set the default log level to DEBUG
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
