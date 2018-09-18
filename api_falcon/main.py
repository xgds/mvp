import falcon
import falcon_cors
import mongoengine
from routes.flight import *
from routes.model  import *
from routes.status import *

mongoengine.connect(
    db='test',
    host='mongo'
)

cors_allow_all = falcon_cors.CORS(
    allow_all_origins=True,
    allow_all_headers=True,
    allow_all_methods=True,
)

api = falcon.API(middleware=[cors_allow_all.middleware])

# ========================================================
api.add_route('/', Status())
# ========================================================
api.add_route('/{model}', Model())
api.add_route('/{model}/{id}', ModelWithID())
# ========================================================
api.add_route('/flight', Flight())
api.add_route('/flight/{id}', FlightWithID())
api.add_route('/flight/{id}/objects', FlightAllObjects())
api.add_route('/flight/{id}/{model}', FlightWithModel())
# ========================================================
