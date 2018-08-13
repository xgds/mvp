from mongoengine import *


class Point(EmbeddedDocument):
    x = FloatField()
    y = FloatField()
    z = FloatField()


class Header(EmbeddedDocument):
    stamp    = DateTimeField()
    frame_id = StringField()


class MeshTriangle(EmbeddedDocument):
    vertex_indices = ListField(IntField())


class Mesh(EmbeddedDocument):
    triangles = EmbeddedDocumentListField(MeshTriangle)
    vertices  = EmbeddedDocumentListField(Point)
