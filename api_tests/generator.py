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

print(r.status_code)

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

while True:
    point_stamped['point']['x'] += 0.001
    point_stamped['point']['y'] += 0.001
    point_stamped['header']['stamp'] = datetime.utcnow().isoformat()
    point_stamped['header']['frame_id'] = hex(int(point_stamped['header']['frame_id'], 16) + 1)

    r = post(
        url=make_url("point_stamped"),
        json=point_stamped,
    )

    assert r.status_code == 201

    sleep(0.1)

    id = r.json()["id"]

    r = get(
        url=make_url("point_stamped", id)
    )

    print(r.json())

    sleep(0.9)

    r = post(
        url=make_url("query"),
        json={
            "input": {
                "model_name": "point_stamped",
                "header": {
                    "stamp": {
                        "lt": datetime.utcnow().isoformat()
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

    print(r.json())

    sleep(1)





