from classes.decorators import for_all_methods, validate_output, validate_input
import falcon
from classes.helpers import fix_before_json

@for_all_methods(validate_input)
@for_all_methods(validate_output)
class SubmodelWithId:
    def on_post(self, request, response):
        new_sub_model = request.sub_model_object(**request.media)
        new_sub_model.save()
        request.sub_model.append(new_sub_model)
        request.object_by_id.save()
        response.media = {"id": new_sub_model.id}
        response.status = falcon.HTTP_CREATED

    def on_get(self, request, response):
        response.media = fix_before_json(request.sub_model.to_mongo())
        response.status = falcon.HTTP_OK

    def on_put(self, request, response):
        sub_model_id_list = [s['id'] for s in request.media]
        sub_model_list = [
            s for s in request.sub_model if s.id in sub_model_id_list]
        for s in sub_model_list:
            updates = [u for u in request.media if u.id == s.id][0]
            for i, j in updates.items():
                s[i] = j
            s.save()
        response.media = {}
        response.status = falcon.HTTP_NO_CONTENT

    def on_delete(self, request, response):
        [s.delete() for s in request.sub_model]
        response.media = {}
        response.status = falcon.HTTP_NO_CONTENT
