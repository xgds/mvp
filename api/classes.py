from flask import request
from flask_restful import Resource
from flask_restful_swagger import swagger
from mongoengine.base import BaseField
from decorators import validate_input, validate_output
import mongoengine
from helper_functions import *


class Status(Resource):
    @swagger.operation()
    def get(self):
        return {}, 204


class ModelName(Resource):
    @validate_input()
    @validate_output()
    @swagger.operation()
    def post(self):
        new_object = request.model_object(**request.validated_json)
        new_object.save()
        return {"id": str(new_object.id)}, 201

    @validate_input()
    @validate_output()
    @swagger.operation()
    def get(self):
        returned_list = request.model_object.objects.all()
        if len(returned_list) == 0:
            return [], 204
        returned_list = [fix_before_json(r.to_mongo()) for r in returned_list]
        return returned_list, 200

    @validate_input()
    @validate_output()
    @swagger.operation()
    def put(self):
        assert isinstance(request.validated_json, list)
        assert len(request.validated_json) > 0
        assert isinstance(request.validated_json[0], dict)
        for new_object in request.validated_json:
            old_object = request.model_object.objects.get(id=new_object["id"])
            for i, j in new_object.items():
                old_object[i] = j
        return {}, 204

    @validate_input()
    @validate_output()
    @swagger.operation()
    def delete(self):
        object_list = request.model_object.objects.all()
        deleted_id = []
        for obj in object_list:
            deleted_id.append(str(obj.id))
            obj.delete()
        if len(deleted_id) == 0:
            return {}, 204
        return {"id": deleted_id}, 200

    @validate_input()
    @validate_output()
    @swagger.operation()
    def options(self):
        returned_json = {}
        for attribute in dir(request.model_object):
            if attribute.startswith("_") or attribute.endswith("_"):
                continue
            field = getattr(request.model_object, attribute)
            type_of_field = field.__class__
            if not issubclass(type_of_field, BaseField):
                continue
            if isinstance(field, mongoengine.ReferenceField):
                references = field.document_type_obj
                returned_json[attribute] = references.__name__
            else:
                returned_json[attribute] = type_of_field.__name__
        return returned_json, 200


class ModelNameWithID(Resource):
    @validate_input()
    @validate_output()
    @swagger.operation()
    def get(self):
        obj = fix_before_json(request.object_by_id.to_mongo())
        obj["id"] = obj["_id"]
        del obj["_id"]
        return obj, 200

    @validate_input()
    @validate_output()
    @swagger.operation()
    def put(self):
        for i, j in request.validated_json.items():
            request.object_by_id[i] = j
        request.object_by_id.save()
        return {}, 204

    @validate_input()
    @validate_output()
    @swagger.operation()
    def delete(self):
        request.object_by_id.delete()
        return {}, 204


class ModelNameWithIDAndSubModel(Resource):
    @validate_input()
    @validate_output()
    @swagger.operation()
    def post(self):
        new_sub_model = request.sub_model_object(**request.validated_json)
        new_sub_model.save()
        request.sub_model.append(new_sub_model)
        request.object_by_id.save()
        return {"id": new_sub_model.id}, 201

    @validate_input()
    @validate_output()
    @swagger.operation()
    def get(self):
        return fix_before_json(request.sub_model.to_mongo()), 200

    @validate_input()
    @validate_output()
    @swagger.operation()
    def put(self):
        sub_model_id_list = [s['id'] for s in request.validated_json]
        sub_model_list = [s for s in request.sub_model if s.id in sub_model_id_list]
        for s in sub_model_list:
            updates = [u for u in request.validated_json if u.id == s.id][0]
            for i, j in updates.items():
                s[i] = j
            s.save()
        return {}, 204

    @validate_input()
    @validate_output()
    @swagger.operation()
    def delete(self):
        [s.delete() for s in request.sub_model]
        return {}, 204
