from djongo.models import *

class Position(Model):
    latitude  = DecimalField(decimal_places=4, max_digits=10)
    longitude = DecimalField(decimal_places=4, max_digits=10)

    def __str__(self):
        return "position with coordinates ({}, {})".format(
            self.latitude,
            self.longitude,
        )

class Flight(Model):
    start   = DateTimeField(auto_now_add=True)
    end     = DateTimeField(auto_now_add=False)

    class Meta:
        ordering = ('start',)

    def __str__(self):
        return "flight starting at {} and ending at {}".format(
            self.start,
            self.end,
        )

class Object(Model):
    time    = DateTimeField(auto_now_add=True)
    name    = CharField(max_length=100, blank=True, default='')
    flight  = ForeignKey(Flight, on_delete=CASCADE)
    point   = ForeignKey(Position, on_delete=CASCADE)

    class Meta:
        ordering = ('time',)

    def __str__(self):
        return "object created at {} with name {}".format(
            self.time,
            self.name,
        )
