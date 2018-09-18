from mongoengine import *
from datetime import datetime
from json import loads

class JsonMixin:
    @classmethod
    def create_from_json(cls, json: dict):
        for key, value in json.items():
            if not isinstance(value, str): continue
            try:
                json[key] = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                pass

        return cls(**json)

    def convert_to_json(self) -> dict:
        return loads(self.to_json())

class Flight(Document, JsonMixin):
    '''
    POST /flight
    {
        "start": "2018-09-09 13:00:29",
        "end":   "2018-10-11 15:01:55"        
    }
    '''
    
    # start and end times of this flight
    start = DateTimeField()
    end   = DateTimeField()
    
class Object(DynamicDocument, JsonMixin):
    '''
    POST /sensor
    {
        "flight": "a16dffa",
        "point": [37.414889, -122.048794],
        "time": "2018-09-09 13:00:29",
        ...
        "temperature": 19.2,
        "humidity": 89
    }
    '''

    # the name of this object
    object_name = StringField(required=True)

    # foreign key to the flight of this object
    flight = ReferenceField(Flight)

    # geospatial and temporal fields
    point = PointField()
    time = DateTimeField()

    # all additional fields can be added because
    # this is a Dynamic Document
