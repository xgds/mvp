from classes.decorators import for_all_methods, validate_input, validate_output
from classes.helpers import create_json_from_object
from models import model_to_dict
import falcon


@for_all_methods(validate_input)
@for_all_methods(validate_output)
class ModelWithId:
    def on_get(self, request, response):
        obj = request.object_by_id
        response.media = model_to_dict(obj)

    def on_put(self, request, response):
        for i, j in request.media.items():
            request.object_by_id[i] = j
        request.object_by_id.save()
        response.media = {}

    def on_delete(self, request, response):
        request.object_by_id.delete()
        response.status = falcon.HTTP_NO_CONTENT
