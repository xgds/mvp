from datetime import datetime, timedelta
import pytz
from requests import post, get, put, delete, options
from pprint import pprint
from time import sleep
import random
import string

min_lat, min_lon = 37.121796, -122.246653
max_lat, max_lon = 37.591179, -121.609724

def random_coordinate():
    lat = random.uniform(min_lat, max_lat)
    lon = random.uniform(min_lon, max_lon)
    return [lon, lat]

def time_from_unix(unix: int) -> str:
    return datetime.utcfromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S")

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

r = delete(
    url=url + "object"
)
assert r.status_code == 204

r = delete(
    url=url + "flight"
)
assert r.status_code == 204

flight_ids_list = []
for _ in range(10):
    starting_t = int((datetime.utcnow() - timedelta(hours=random.randint(0, 100))).timestamp())
    ending_t   = int((datetime.utcfromtimestamp(starting_t) + timedelta(hours=random.randint(1, 6)) + timedelta(minutes=random.randint(0, 60))).timestamp())

    r = post(
        url=url + "flight",
        json={
            "start": time_from_unix(starting_t),
            "end":   time_from_unix(ending_t),
        }
    )
    assert r.status_code == 201

    flight_id = r.json()["id"]
    flight_ids_list.append(flight_id)

    r = post(
        url=url + "sensor",
        json={
            "flight": flight_id,
            "point": random_coordinate(),
            "time": time_from_unix(random.randint(starting_t, ending_t)),
            "temperature": random.uniform(-20, 100),
            "humidity": random.randint(1, 99),
        }
    )
    assert r.status_code == 201

    r = post(
        url=url + "note",
        json={
            "flight": flight_id,
            "point": random_coordinate(),
            "time": time_from_unix(random.randint(starting_t, ending_t)),
            "text": "this is an interesting observation!",
            "user": "Khaled the Wise",
        }
    )
    assert r.status_code == 201

    r = post(
        url=url + "camera",
        json={
            "flight": flight_id,
            "point": random_coordinate(),
            "time": time_from_unix(random.randint(starting_t, ending_t)),
            "file": "a81ff00",
            "exposure": 2,
            "aperture": "f/1.8",
        }
    )
    assert r.status_code == 201

    r = get(
        url=url + "flight/" + flight_id + "/objects"
    )
    assert r.status_code == 200

print(flight_ids_list)