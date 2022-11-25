__author__ = 'Thilina_08838'

from flask import *

import urllib.request
from urllib.request import urlopen

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    text1 = 'Hello World'
    return text1


@app.route('/lbsSender', methods=["GET", "POST"])
def lbs_request():

        res = {
                "applicationId": "APP_007453", # Use your app ID
                "password": "a04e5780809a11f71ff092d42c711518", # Use your app password
                "subscriberId": "tel:94717865103", # Use the MSISDN in the format you received
                 "requesterId": "tel94717865103",
                }

        with open("LBSRequest.txt", "w") as text_file:
            print("LBS request: {}".format(res), file=text_file)
        url = "https://api.mspace.lk/lbs/request" # Use production URL in the live system

        res = json.dumps(res).encode('utf8')
        req = urllib.request.Request(url, res, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response = urlopen(req)
        ideamart_respones = response.read()
        with open("LBSResponse.txt", "w") as text_file:
            print("LBS response: {}".format(ideamart_respones), file=text_file)

if __name__ == '__main__':
    app.run(host="localhost", port=5000)

