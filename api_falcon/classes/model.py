from classes.decorators import *
from classes.helpers import *
import sys
import falcon

@for_all_methods(validate_input)
@for_all_methods(validate_output)
class Model:
    def on_get(self, request, response):
        returned_list = request.model_class.objects.all()
        if len(returned_list) == 0:
            response.media = []
            response.status = falcon.HTTP_NO_CONTENT
        else:
            returned_list = [fix_before_json(r.to_mongo()) for r in returned_list]
            response.media = returned_list
            response.status = falcon.HTTP_OK

    def on_post(self, request, response):
        new_object = request.model_class.dict_to_model(dictionary=request.media)
        new_object.save()
        response.media = {"id": str(new_object.id)}
        response.status = falcon.HTTP_CREATED

    def on_put(self, request, response):
        for new_object in request.media:
            old_object = request.model_class.objects.get(id=new_object["id"])
            for i, j in new_object.items():
                old_object[i] = j
        response.media = []
        response.status = falcon.HTTP_NO_CONTENT

    def on_delete(self, request, response):
        object_list = request.model_class.objects.all()
        deleted_id = []
        for obj in object_list:
            deleted_id.append(str(obj.id))
            obj.delete()
        if len(deleted_id) == 0:
            response.media = []
            response.status = falcon.HTTP_NO_CONTENT
        else:
            response.media = {"id": deleted_id}
            response.status = falcon.HTTP_OK

    def on_options(self, request, response):
        returned_json = {}
        for attribute in dir(request.model_class):
            if attribute.startswith("_") or attribute.endswith("_"):
                continue
            field = getattr(request.model_class, attribute)
            type_of_field = field.__class__
            if not issubclass(type_of_field, BaseField):
                continue
            if isinstance(field, mongoengine.ReferenceField):
                references = field.document_type_obj
                returned_json[attribute] = references.__name__
            else:
                returned_json[attribute] = type_of_field.__name__
        response.media = returned_json