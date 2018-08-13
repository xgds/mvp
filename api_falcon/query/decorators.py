from functools import wraps
import falcon
from query.helpers import to_camel_case, get_class
from query.models import Query


def query_creation():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self, request, response = args[0:3]
            assert (isinstance(request, falcon.Request))
            assert (isinstance(response, falcon.Response))
            json = request.media
            assert isinstance(json, dict)
            assert "input" in json
            assert "output" in json
            request.query_input = json["input"]
            request.query_output = json["output"]
            model_name = to_camel_case(request.query_input["model_name"])
            try:
                request.model_class = get_class(model_name)
            except AttributeError:
                raise falcon.HTTPNotFound()
            return func(self, request, response)

        return wrapper

    return decorator


def query_fetch():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self, request, response = args[0:3]
            assert isinstance(request, falcon.Request)
            assert isinstance(response, falcon.Response)
            request.query_by_id = Query.objects.get(id=kwargs["id"])
            return func(self, request, response)

        return wrapper

    return decorator
