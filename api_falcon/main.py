import falcon
import mongoengine
from classes.model import Model
from classes.model_with_id import ModelWithId
from classes.submodel_with_id import SubmodelWithId
from classes.status import Status
from query.classes import QueryCreation, QueryFetch

processing_threads = []

mongoengine.connect(
    db='test',
    host='mongo'
)

api = falcon.API()
api.add_route('/', Status())
api.add_route('/{model_name}', Model())
api.add_route('/{model_name}/{id}', ModelWithId())
api.add_route('/{model_name}/{id}/{sub_model_name}', SubmodelWithId())
api.add_route('/query', QueryCreation())
api.add_route('/query/{id}', QueryFetch())
