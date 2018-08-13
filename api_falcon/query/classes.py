from query.decorators import query_creation, query_fetch
from query.models import Query, QueryInput
from threading import Thread
import falcon
from query.helpers import process_query
from assertpy import assert_that


class QueryCreation:
    @query_creation()
    def on_post(self, request, response):
        new_query = Query()
        query_input = QueryInput(**request.query_input)
        query_input.save()
        new_query.query_input = query_input
        new_query.save()
        query_id = str(new_query.id)
        new_thread = Thread(target=process_query, args=(query_id,))
        new_thread.start()
        response.media = {"id": query_id}
        response.status = falcon.HTTP_CREATED


class QueryFetch:
    @query_fetch()
    def on_get(self, request, response):
        if request.query_by_id.complete:
            assert_that(request.query_by_id.query_result.result).is_instance_of(list)
            response.media = [convert_object_to_json(q.to_mongo()) for q in request.query_by_id.query_result.result]
            response.status = falcon.HTTP_OK
        else:
            response.media = {}
            response.status = falcon.HTTP_ACCEPTED
