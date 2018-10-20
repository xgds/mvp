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
    url=make_url("geo_point_stamped")
)

datetime_now = datetime.utcfromtimestamp(0)

while True:
    r = post(
        url=make_url("query"),
        json={
            "input": {
                "model_name": "geo_point_stamped",
                "header": {
                    "stamp": {
                        "gt": datetime_now.isoformat(),
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

    if len(json) > 0:    
        datetime_now = datetime.fromisoformat(sorted(json, key=lambda x: x['header']['stamp'])[-1]['header']['stamp'])
    
    sleep(2)


