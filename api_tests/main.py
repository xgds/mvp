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


def make_url(model_name: str, uuid: str = None, sub_model_name: str = None) -> str:
    u = url + model_name

    if sub_model_name is not None:
        return u + "/" + uuid + "/" + sub_model_name

    if uuid is not None:
        return u + "/" + uuid

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
print(r.json())

uuid = r.json()["uuid"]

r = get(
    url=make_url("header", uuid)
)

print(r.status_code)
print(r.json())

r = put(
    url=make_url("header", uuid),
    json={
        "frame_id": "b2b",
    }
)

print(r.status_code)
print(r.content)

r = get(
    url=make_url("header", uuid)
)

print(r.status_code)
print(r.json())

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
    url=make_url("path")
)

print(r.status_code)
pprint(r.json())
