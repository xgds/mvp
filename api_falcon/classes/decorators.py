from functools import wraps
import falcon
from helpers import *


def validate_input():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self, request, response = args[0:3]
            assert isinstance(request, falcon.Request)
            assert isinstance(response, falcon.Response)
            model_name = to_camel_case(kwargs["model_name"])
            try:
                request.model_class = get_class(model_name)
            except AttributeError:
                raise falcon.HTTPNotFound()
            try:
                if request.media:
                    fix_datetime_fields(request.media, request.model_class)
            except:
                pass
            if "id" in kwargs:
                object_by_id = request.model_class.objects.filter(id=kwargs["id"])
                if len(object_by_id) == 0:
                    raise falcon.HTTPNotFound()
                if len(object_by_id) > 1:
                    raise falcon.HTTPInternalServerError()
                request.object_by_id = object_by_id[0]
            return func(self, request, response)

        return wrapper

    return decorator


def validate_output():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator()(getattr(cls, attr)))
        return cls

    return decorate
