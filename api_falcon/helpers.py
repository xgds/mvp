from inspect import isclass
from mongoengine import Document, DateTimeField
import models
import re
from bson import ObjectId
from datetime import datetime
import collections
from mongoengine.base import BaseField
import mongoengine


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


