from inspect import isclass
from mongoengine import DateTimeField
import models
import re
from bson import ObjectId
from datetime import datetime
import collections
from mongoengine.base import BaseField
import mongoengine


def value_to_json(value):
    if isinstance(value, datetime):
        return str(value.isoformat())
    elif isinstance(value, ObjectId):
        return str(value)
    else:
        return value


def create_json_from_object(obj):
    returned_json = {}
    attributes = [
        (x, getattr(obj, x)) for x in dir(obj)
        if not x.startswith("_") and not x.endswith("_")
    ]
    for name, value in attributes:
        if not issubclass(getattr(obj.__class__, name).__class__, BaseField):
            continue
        if isinstance(getattr(obj.__class__, name), mongoengine.EmbeddedDocumentField):
            returned_json[name] = create_json_from_object(value)
        elif isinstance(getattr(obj.__class__, name), mongoengine.ListField):
            returned_json[name] = [create_json_from_object(x) for x in value]
        else:
            returned_json[name] = value_to_json(value)
    return returned_json


def create_object_from_json(new_class, json: dict):
    assert isclass(new_class)
    assert isinstance(json, dict)
    parent_attributes = {}
    child_attributes = []
    for i, j in json.items():
        if isinstance(j, dict):
            child_attributes.append((i, j))
        else:
            parent_attributes[i] = j
    new_object = new_class(**parent_attributes)
    if len(child_attributes) > 0:
        for class_name, class_initializer in child_attributes:
            class_object = get_class(to_camel_case(class_name))
            assert class_object is not None
            assert isclass(class_object)
            fix_datetime_fields(class_initializer, class_object)
            setattr(new_object, class_name, class_object(**class_initializer))
    new_object.save()
    return new_object


def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def fix_datetime_fields(json, model_object):
    assert isinstance(json, dict)
    assert isclass(model_object)
    for i, j in json.items():
        if isinstance(getattr(model_object, i), DateTimeField):
            if not isinstance(j, dict):
                json[i] = datetime.fromisoformat(j)
            else:
                json[i] = {k:datetime.fromisoformat(v) for k, v in j.items()}


def to_snake_case(s: str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def to_camel_case(s):
    return ''.join(x.title() for x in s.split("_"))


def get_class(s: str):
    try:
        c = getattr(models, s)
        assert isclass(c), "C was not a class!"
    except AttributeError:
        return None
    return c


def fix_before_json(obj: dict) -> dict:
    assert isinstance(obj, dict), "obj: {}, type(obj): {}".format(
        obj, type(obj))
    new_obj = {}
    for i, j in obj.items():
        if isinstance(j, dict):
            new_obj[i] = fix_before_json(j)
        elif isinstance(j, ObjectId):
            new_obj[i] = str(j)
        elif isinstance(j, datetime):
            new_obj[i] = j.isoformat()
    return new_obj


def convert_object_to_json(q):
    from bson.son import SON
    json = {}
    for i, j in q.items():
        if   isinstance(j, SON):      json[str(i)] = convert_object_to_json(j.to_dict())
        elif isinstance(j, dict):     json[str(i)] = convert_object_to_json(j)
        elif isinstance(j, datetime): json[str(i)] = j.isoformat()
        elif isinstance(j, ObjectId): json[str(i)] = str(j)
        else: json[str(i)] = j
    if "_id" in json:
        json["id"] = json["_id"]
        del json["_id"]
    if "_cls" in json:
        del json["_cls"]
    return json
