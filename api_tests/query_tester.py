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
    make_url("point_stamped")
)

latitude, longitude = 37.419670, -122.064930

point_stamped = {
    "header": {
        "stamp": datetime.utcnow().isoformat(),
        "frame_id": "0xa1a",
    },
    "point": {
        "x": longitude,
        "y": latitude,
        "z": 0.0,
    }
}

ids = []
point_stamped['header']['stamp'] = datetime(2018, 1, 2).isoformat()
point_stamped['header']['frame_id'] = hex(4815)
r = post(
    url=make_url("point_stamped"),
    json=point_stamped,
)
assert r.status_code == 201
ids.append(r.json()["id"])

point_stamped['header']['stamp'] = datetime(2018, 2, 2).isoformat()
point_stamped['header']['frame_id'] = hex(1623)
r = post(
    url=make_url("point_stamped"),
    json=point_stamped,
)
assert r.status_code == 201
ids.append(r.json()["id"])

point_stamped['header']['stamp'] = datetime(2018, 3, 2).isoformat()
point_stamped['header']['frame_id'] = hex(4248)
r = post(
    url=make_url("point_stamped"),
    json=point_stamped,
)
assert r.status_code == 201
ids.append(r.json()["id"])

for id in ids:
    r = get(
        make_url("point_stamped", id)
    )
    print(r.status_code)
    print(r.json())

# exit()

sleep(1)

r = post(
    url=make_url("query"),
    json={
        "input": {
            "model_name": "point_stamped",
            "header": {
                "stamp": {
                    "lt": datetime(2018, 3, 1).isoformat(),
                    "gt": datetime(2018, 1, 3).isoformat(),
                }
            }
        },
        "output": {}
    }
)

assert r.status_code == 201, r.content

id = r.json()["id"]

sleep(1)

r = get(
    url=make_url("query", id)
)

assert r.status_code == 200, "content: {}, status_code: {}".format(r.content, r.status_code)

json = r.json()
print(json)
print(r.content)
assert len(json) == 1
assert json[0]['header']['frame_id'] == hex(1623)







