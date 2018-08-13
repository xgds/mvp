from mongoengine import *
import mongoengine
from datetime import datetime
import embedded_models

class CustomDynamicDocument(DynamicDocument):
    meta = {'allow_inheritance': True}

    @classmethod
    def dict_to_model(cls, dictionary, model=None):
        from inspect import isclass
        if model is None:
            model = cls
        assert isclass(model)
        assert isinstance(dictionary, dict)
        for i, j in dictionary.items():
            if isinstance(j, dict):
                dictionary[i] = cls.dict_to_model(j, getattr(model, i).document_type_obj)
            elif isinstance(j, list):
                if isinstance(getattr(model, i), EmbeddedDocumentListField):
                    dictionary[i] = [cls.dict_to_model(k, getattr(model, i).field.document_type_obj) for k in j]
                else:
                    # we should be fine
                    pass
            elif isinstance(j, str):
                if isinstance(getattr(model, i), DateTimeField):
                    dictionary[i] = datetime.fromisoformat(j)
        return model(**dictionary)


def model_to_dict(obj):
    cls = obj.__class__

    # ==========================================
    # debugging; remove later
    # ==========================================
    import sys
    print("class: {}, obj: {}".format(cls, obj))
    sys.stdout.flush()
    # ==========================================
    
    def fix_before_json(j):
        from bson import ObjectId
        if isinstance(j, ObjectId):
            return str(j)
        if isinstance(j, datetime):
            return j.isoformat()
        return j

    if type(obj) in [int, float, str]:
        return obj
    
    if isinstance(obj, datetime):
        return datetime.isoformat()

    if issubclass(cls, mongoengine.base.BaseList):
        return [model_to_dict(o) for o in obj]
    
    returned_json = {}
    attributes = [
        (x, getattr(obj, x)) for x in dir(obj)
        if not x.startswith("_") and not x.endswith("_")
    ]
    for name, value in attributes:
        name_as_attribute = getattr(cls, name)
        if  not issubclass(name_as_attribute.__class__, mongoengine.base.BaseField):
            continue
        if isinstance(name_as_attribute, mongoengine.EmbeddedDocumentField):
            returned_json[name] = model_to_dict(value)
        elif isinstance(name_as_attribute, mongoengine.EmbeddedDocumentListField):
            returned_json[name] = [model_to_dict(value) for x in value]
        else:
            returned_json[name] = fix_before_json(value)
    return returned_json




class PointStamped(CustomDynamicDocument):
    header = EmbeddedDocumentField(embedded_models.Header)
    point  = EmbeddedDocumentField(embedded_models.Point)


class Mesh(CustomDynamicDocument):
    triangles = EmbeddedDocumentListField(embedded_models.MeshTriangle)
    vertices  = EmbeddedDocumentListField(embedded_models.Point)
