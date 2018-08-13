from query.decorators import *
from helpers import to_camel_case, get_class, flatten
from inspect import isclass
from datetime import datetime
from query.models import Query, QueryResult

def detect_and_fix_datetime(s: str):
    if len(s) == 19 and s.count("-") == 2 and s.count("T") == 1 and s.count(":") == 2:
        return datetime.fromisoformat(s)
    return None

def fix_json_query(json_query: dict) -> dict:
    assert isinstance(json_query, dict)

    if "_id" in json_query:
        del json_query["_id"]

    flattened = flatten(json_query, sep="__")

    for i, j in flattened.items():
        dt = detect_and_fix_datetime(j)
        if dt is not None:
            flattened[i] = dt

    return flattened


def mark_query_complete(query_id: str) -> None:
    query = Query.objects.get(id=query_id)
    query.complete = True
    query.save()


def process_query(query_id: str) -> None:
    query = Query.objects.get(id=query_id)
    model_class = get_class(to_camel_case(query.query_input.model_name))
    assert model_class is not None
    assert isclass(model_class)
    query_input = query.query_input.to_mongo()
    assert isinstance(query_input, dict)
    del query_input["model_name"]
    query_input = fix_json_query(query_input)
    query_result = model_class.objects(**query_input)
    query_result = QueryResult(result=query_result)
    query_result.save()
    query.query_result = query_result
    query.save()
    mark_query_complete(query_id)
