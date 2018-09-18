import falcon
import falcon_cors
import models

class Model:
    # return all instances of model
    def on_get(self, request, response, model):
        response.media  = [x.convert_to_json() for x in models.Object.objects(object_name=model)]
        response.status = falcon.HTTP_OK if len(response.media) > 0 else falcon.HTTP_NO_CONTENT

    # create new instance of a model
    def on_post(self, request, response, model):
        request.media["object_name"] = model
        request.media["flight"] = models.Flight.objects(id=request.media["flight"])[0]
        new_object = models.Object.create_from_json(request.media)
        new_object.save()
        response.media  = {"id": str(new_object.id)}
        response.status = falcon.HTTP_CREATED

    # delete all instances of a model
    def on_delete(self, request, response, model):
        object_list = models.Object.objects(object_name=model)
        [o.delete() for o in object_list]
        response.status = falcon.HTTP_NO_CONTENT

class ModelWithID:
    # return specific instance of model
    def on_get(self, request, response, model, id):
        response.media  = models.Object.objects(object_name=model, id=id)[0].convert_to_json()
        response.status = falcon.HTTP_OK

    # delete specific instance of model
    def on_delete(self, request, response, model, id):
        models.Object.objects(object_name=model, id=id)[0].delete()
        response.status = falcon.HTTP_NO_CONTENT

