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


r = post(
    url=make_url("header"),
    json={
        "stamp": datetime(2018, 9, 10, tzinfo=pytz.UTC).isoformat(),
        "frame_id": "a1a",
    }
)

print(r.status_code)
print(r.content)

id = r.json()["id"]

r = get(
    url=make_url("header", id)
)

print(r.status_code)
print(r.content)

r = put(
    url=make_url("header", id),
    json={
        "frame_id": "b2b",
    }
)

print(r.status_code)
print(r.content)

r = get(
    url=make_url("header", id)
)

print(r.status_code)
print(r.content)

r = delete(
    url=make_url("header")
)

print(r.status_code)
print(r.content)

r = get(
    url=make_url("header")
)

print(r.status_code)
print(r.content)

r = options(
    url=make_url("point_stamped")
)

print(r.status_code)
print(r.content)

point_stamped = {
    "header": {
        "stamp": datetime.utcnow().isoformat(),
        "frame_id": "a1a",
    },
    "point": {
        "x": -50,
        "y":  60,
        "z": -15,
    }
}

r = post(
    url=make_url("point_stamped"),
    json=point_stamped,
)

print(r.status_code)
print(r.content)


id = r.json()["id"]

r = get(
    url=make_url("point_stamped", id)
)

print(r.status_code)
print(r.content)
print()
pprint(r.json())
