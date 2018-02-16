from flask import Flask
from flask import Response
import json
import detect
import eye

app = Flask(__name__)

@app.route("/")
def detect_label():
    eye.take_photo()
    labels = detect.detect_labels("img/tmp.png")
    descriptions = [label.description for label in labels]
    str_concat = lambda x, y: x + ', ' + y
    items_msg = "I saw %s"%reduce(str_concat, descriptions)
    # js_response = json.dumps({'speech':items_msg, 'displayText':items_msg}) 
    # resp = Response(js_response, status=200, mimetype='application/json')
    #return resp 
    return items_msg


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080, debug=False)
        #app.run(host='0.0.0.0', port=8080, debug=False, ssl_context=('cert.pem', 'key.pem'))
