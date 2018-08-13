from datetime import datetime
import pytz
from requests import post, get, put, delete, options
from pprint import pprint
from time import sleep

url = "http://api:5000/"

while True:
    try:
        r = get(url)
        assert r.status_code == 204
        break
    except:
        sleep(0.25)

def make_url(model_name: str, id: str = None, sub_model_name: str = None) -> str:
    u = url + model_name

    if sub_model_name is not None:
        return u + "/" + id + "/" + sub_model_name

    if id is not None:
        return u + "/" + id

    return u

r = delete(
    make_url("mesh")
)

latitude, longitude = 37.419670, -122.064930

mesh = {
    "triangles": [
        {
            "vertex_indices": [4, 8, 15, 16, 23, 42]
        }
    ],
    "vertices": [
        {
            "x": 4,
            "y": 8,
            "z": 15,
        }
    ],
}

r = post(
    make_url("mesh"),
    json=mesh,
)

print(r.status_code)
print(r.content)

id = r.json()["id"]

r = get(
    make_url("mesh", id)
)

print(r.status_code)
print(r.json())


