from functools import wraps
from flask import request, abort
from helper_functions import *


def validate_input():
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            if "model_name" in kwargs:
                if not hasattr(models, to_camel_case(kwargs["model_name"])):
                    abort(404)
            else:
                abort(500)

            request.model_object = get_class(to_camel_case(kwargs["model_name"]))

            if "id" in kwargs:
                object_by_id = request.model_object.objects.filter(id=kwargs["id"])
                if len(object_by_id) == 0:
                    abort(404)
                if len(object_by_id) > 1:
                    abort(500)
                request.object_by_id = object_by_id[0]

            if "sub_model_name" in kwargs:
                try:
                    sub_model = getattr(request.object_by_id, kwargs["sub_model_name"])
                except AttributeError:
                    abort(404)
                request.sub_model = sub_model

            try:
                request.validated_json = request.get_json()
            except:
                request.validated_json = None

            if request.validated_json is not None:
                request.validated_json = fix_datetime_fields(request.validated_json, request.model_object)

            # this is equal to func(self)
            return func(args[0])

        return wrapper

    return decorator


def validate_output():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            returned_value = func(*args, **kwargs)

            assert isinstance(returned_value, tuple)
            assert len(returned_value) == 2
            assert isinstance(returned_value[0], list) or isinstance(returned_value[0], dict)
            assert isinstance(returned_value[1], int)
            assert 200 <= returned_value[1] < 600

            return returned_value

        return wrapper

    return decorator
