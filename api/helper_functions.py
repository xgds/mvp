from inspect import isclass
from mongoengine import Document, DateTimeField
import models
import re
from bson import ObjectId
import datetime


def fix_datetime_fields(json, model_object):
    for i, j in json.items():
        if isinstance(getattr(model_object, i), DateTimeField):
            json[i] = datetime.datetime.fromisoformat(j)
    return json


def to_snake_case(s: str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def to_camel_case(s):
    return ''.join(x.title() for x in s.split("_"))


def get_class(s: str):
    try:
        c = getattr(models, s)
        assert isclass(c), "C was not a class!"
        assert issubclass(c, Document), "C is not a subclass of a MongoEngine Document, it is a {}!".format(type(c))
    except AttributeError:
        return None
    return c


def fix_before_json(obj: dict):
    for i, j in obj.items():
        if isinstance(j, ObjectId):
            obj[i] = str(j)
        elif isinstance(j, datetime.datetime):
            obj[i] = j.isoformat()
    return obj
