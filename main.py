import requests
import os
import datetime
from requests_oauthlib import OAuth1
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def run_tw():
    client_key = '7BUrIbCEngSuXlxzGdW2vh2cd'
    client_secret = 'wy8LzEwFLZ6ATFmddwEn5qQIFV5OsVG4Vrjnjr8B5Rac8Y6l8s'
    resource_owner_key = '1240640391482953730-CEMHlT0tLo92Zc3W4KGZjwMunBmmzV'
    resource_owner_secret = 'tpOx2CgYheUPkaFv8HRFK9I42QFPmqMGhH17hkG2OTFjB'
    ACCOUNT_ID = '25705856'

    # Twitter Required Date
    iso_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%sZ")

    # Twitter Required Twitter ClickId
    def get_twclid():
        args = request.args
        twclid = args.get('twclid')
        if twclid is None:
            twclid = "12345" #dummy
        return twclid

    payload = {'conversions': [
        {'conversion_time': iso_date,
         'event_id': 'tw-o8xqn-ocl08',
         'identifiers': [
             {'twclid': get_twclid()
              }
         ]
         }
    ]}

    url = 'https://ads-api.twitter.com/11/measurement/conversions/o8xqn'
    headeroauth = OAuth1(client_key,
                         client_secret,
                         resource_owner_key,
                         resource_owner_secret,
                         signature_type='auth_header')
    r = requests.post(url, auth=headeroauth, json=payload)
    return r.text


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))