import inspect
import models
import re


def to_snake_case(s: str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def to_camel_case(s):
    return ''.join(x.title() for x in s.split("_"))


for c in dir(models):
    if inspect.isclass(getattr(models, c)):
        print(c, to_camel_case(to_snake_case(c)))
