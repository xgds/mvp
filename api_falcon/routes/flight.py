import falcon
import falcon_cors
import models

class Flight:
    # return all flights
    def on_get(self, request, response):
        response.media  = [x.convert_to_json() for x in models.Flight.objects]
        response.status = falcon.HTTP_OK if len(response.media) > 0 else falcon.HTTP_NO_CONTENT

    # create new instance of a model
    def on_post(self, request, response):
        new_object = models.Flight.create_from_json(request.media)
        new_object.save()
        response.media  = {"id": str(new_object.id)}
        response.status = falcon.HTTP_CREATED

    # delete all instances of a model
    def on_delete(self, request, response):
        [o.delete() for o in models.Flight.objects]
        response.status = falcon.HTTP_NO_CONTENT

class FlightWithID:
    # return specific flight
    def on_get(self, request, response, id):
        response.media  = models.Flight.objects(id=id)[0].convert_to_json()
        response.status = falcon.HTTP_OK

    # delete specific flight
    def on_delete(self, request, response, id):
        models.Flight.objects(id=id)[0].delete()
        response.status = falcon.HTTP_NO_CONTENT

class FlightAllObjects:
    # return all objects for a specific flight
    def on_get(self, request, response, id):
        all_objects = [x.convert_to_json() for x in models.Object.objects(flight=models.Flight.objects(id=id)[0])]
        assert len(all_objects) > 0 
        returned_objects = {}
        for obj in all_objects:
            object_name = obj["object_name"]
            del obj["object_name"]
            if object_name in returned_objects:
                returned_objects[object_name].append(obj)
            else:
                returned_objects[object_name] = [obj]
        response.media = returned_objects
        response.status = falcon.HTTP_OK if len(response.media) > 0 else falcon.HTTP_NO_CONTENT

class FlightWithModel:
    # return all instances of model for a specific flight
    def on_get(self, request, response, id, model):
        response.media  = [y.convert_to_json() for y in [x for x in models.Object.objects(flight__id=id) if x.object_name == model]]
        response.status = falcon.HTTP_OK if len(response.media) > 0 else falcon.HTTP_NO_CONTENT
