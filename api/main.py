from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger

import mongoengine
from classes import Status, ModelName, ModelNameWithID, ModelNameWithIDAndSubModel

mongoengine.connect(
    db='test',
    host='mongo'
)

app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='1.0')

api.add_resource(
    Status, '/'
)
api.add_resource(
    ModelName, '/<string:model_name>',
)
api.add_resource(
    ModelNameWithID, '/<string:model_name>/<string:id>',
)
api.add_resource(
    ModelNameWithIDAndSubModel, '/<string:model_name>/<string:id>/<string:sub_model_name>',
)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
