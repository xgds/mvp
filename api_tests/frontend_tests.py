from datetime import datetime, timedelta
import pytz
from requests import post, get, put, delete, options
from pprint import pprint
from time import sleep
import random
import string

url = "http://api:5000/"

while True:
    try:
        r = get(url)
        assert r.status_code == 204
        break
    except:
        sleep(0.25)

def random_string():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

r = post(
    url=url + "flight",
    json={
        "start": "2018-09-09 13:00:29",
        "end":   "2018-10-11 15:01:55"        
    }
)
assert r.status_code == 201

flight_id = r.json()["id"]

r = post(
    url=url + "sensor",
    json={
        "flight": flight_id,
        "point": [-122.048794, 37.414889],
        "time": "2018-09-09 13:00:29",
        "temperature": 19.2,
        "humidity": 89
    }
)

r = get(
    url=url + "flight/" + flight_id + "/objects"
)

print(r.json())