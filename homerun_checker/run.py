"""
MLB Data Request Function
"""

import sys, os, requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'lib')))
import json


request = requests.get("http://gd2.mlb.com/components/game/mlb/notifications.json")
data = request.json()
body={}

if 'pbp' in data['data']['alerts']['last_pbp']:
    notifications = data['data']['alerts']['last_pbp']['pbp']

    for x in notifications:
        if "home run" in x['text'].split(" "):
            body.append(x)
else:
    body['text'] = "No Home Runs"

# All data to be returned to the client gets put into this dict
returnData = {
    #HTTP Status Code:
    "status": 200,
    
    #Response Body:
    "body": json.dumps(body),
    
    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "text/html",
        "X-Awesome-Header": "YesItIs"
    }
}

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))