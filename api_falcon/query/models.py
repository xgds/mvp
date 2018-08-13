from mongoengine import *

class QueryInput(DynamicDocument):
    pass


class QueryOutput(Document):
    field_names = ListField(StringField())


class QueryResult(DynamicDocument):
    result = ListField()


class Query(Document):
    query_input = ReferenceField(QueryInput)
    query_output = ReferenceField(QueryOutput)
    query_result = ReferenceField(QueryResult)
    complete = BooleanField(default=False)

